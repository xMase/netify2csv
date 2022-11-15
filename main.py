import getopt
import json
import csv
import logging as logger
import sys

logger.basicConfig(
    level=logger.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logger.FileHandler("debug.log"),
        logger.StreamHandler()
    ]
)


def pcap_anal(inputfilepcap, outputfile):
    # parse socat_proc output to an array
    with open(inputfilepcap, 'r') as file:
        file.seek(0)
        all_detected_flows = []
        inc_id = 0
        for line in file:
            # save relevant flow data to an array
            try:
                jcontent = json.loads(line)
                if 'flow' in jcontent:
                    flow = jcontent['flow']
                    if 'detected_application_name' in flow:
                        ssl = flow['ssl'] if 'ssl' in flow else None
                        all_detected_flows.append([
                            inc_id,
                            flow['host_server_name'] if 'host_server_name' in flow else None,
                            ssl['client_sni'] if ssl and 'client_sni' in ssl else None,
                            flow['detected_application_name'],
                            flow['local_ip'],
                            flow['local_port'],
                            flow['other_ip'],
                            flow['other_port'],
                            flow['ip_protocol'],
                            flow['detected_protocol_name']
                        ])
                        # increment id
                        inc_id += 1
            except:
                logger.debug("Skipping %s", str(line))

        # cleanup tmp file
        logger.info('all_detected_flows %d', len(all_detected_flows))

        # write to csv for fast comparison
        with open(outputfile, 'w') as file:
            writer = csv.writer(file, delimiter=',',
                                lineterminator='\n', quoting=csv.QUOTE_ALL)
            writer.writerows(all_detected_flows)

            logger.info('Output file is %s', outputfile)


def main():
    try:
        opts, _ = getopt.getopt(
            sys.argv[1:], "i:o", ["input=", "output="])

        for o, a in opts:
            if o in ("-i", "--input"):
                input_arg = a
            elif o in ("-o", "--output"):
                output_arg = a
            else:
                assert False, "unhandled option"

        # start processing
        logger.info('Start parsing with netify_proc: %s', input_arg)
        pcap_anal(input_arg, output_arg)
    except getopt.GetoptError as err:
        print(err)


if __name__ == "__main__":
    main()
