#!/usr/bin/env python

import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()

    storage_type = parser.add_mutually_exclusive_group(required=True)
    storage_type.add_argument('--github',
                              dest="github_storage",
                              action='store_true')
    storage_type.add_argument('--aws',
                              dest="aws_storage",
                              action='store_true')

    parser.add_argument('--debug',
                        dest="debug",
                        action='store_true')

    return vars(parser.parse_args())
