# NETIFY SOCKET TO CSV

Collects data from a netify socket and writes it to a csv file.

## Requirements

- Docker

## Usage

```bash
$ ./start-demo.sh
```

The script will start a netify socket and a netify collector. The collector will write the data to a csv file inside the `output` folder (`output.csv`).

## Files

- `start-demo.sh` - Starts the netify socket and the netify collector
- `output/tmp-output.csv` - The output file of the netify socket
- `output/output.csv` - The output file of the netify collector
- `res/large.pcap` - A large pcap file to test the collector
