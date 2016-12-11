import logging
import os
import argparse

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '--output_path',
        type=str,
        help='The path to which checkpoints and other outputs '
        'should be saved. This can be either a local or GCS '
        'path.',
        default=None
    )
    args, _ = argparser.parse_known_args()
    os.makedirs(args.output_path)
    logging.info('BJATHQXM done')
