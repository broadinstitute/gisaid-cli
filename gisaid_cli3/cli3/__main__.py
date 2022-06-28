#!/usr/bin/env python3

"""
    Upload consensus sequences and metadata to GISAID's EpiCoV
    Copyright (C) 2022 Freunde von GISAID e.V.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

DEFAULT_TOKEN = "./gisaid.authtoken"

from datetime import datetime
from pathlib import PurePath
import sys
import json

STARTTIME = datetime.now()
TAB = "\t"


def get_execution_time():
    "Print total runtime at end of run."
    print(f"\nTotal runtime (HRS:MIN:SECS): {str(datetime.now() - STARTTIME)}")

def args_parser():
    """
    Argument parser setup and build.
    """
    import argparse, textwrap
    parser = argparse.ArgumentParser(prog = "cli3",
                                     formatter_class = argparse.ArgumentDefaultsHelpFormatter,
                                     description="Version 3 Command Line Interface (CLI) for uploading sequence and metadata to GISAID.")
    subparser_args1 = argparse.ArgumentParser(add_help=False)
    subparser_args2 = argparse.ArgumentParser(add_help=False)
    subparser_args3 = argparse.ArgumentParser(add_help=False)
    subparser_args4 = argparse.ArgumentParser(add_help=False)
    subparser_args5 = argparse.ArgumentParser(add_help=False)
    subparser_args6 = argparse.ArgumentParser(add_help=False)
    subparser_args7 = argparse.ArgumentParser(add_help=False)
    subparser_args1.add_argument("--database", help="Target GISAID database.",
                                 default = "EpiCoV",
                                 choices = ["EpiCoV", "EpiFlu", "EpiRSV"])
    subparser_args2.add_argument("--token",
                                 help = "Authentication token.",
                                 default = DEFAULT_TOKEN)
    subparser_args3.add_argument("--username",
                                 help = "Your GISAID username. Leave blank on shared computers.",
                                 type = str)
    subparser_args3.add_argument("--password",
                                 help = "Your GISAID password. Leave blank on shared computers.",
                                 type = str)
    subparser_args3.add_argument("--client_id",
                                 help = "Submitter's client-ID. Leave blank on shared computers. Email clisupport@gisaid.org to request client-ID.")
    subparser_args3.add_argument("--force",
                                 help = "Switch on force overwrite of token given at --token",
                                 action = "store_true")
    subparser_args4.add_argument("--log",
                                 help = "All output logged here.",
                                 default = "./logfile.log")
    subparser_args5.add_argument("--template",
                                 help = "Print submission 'template.csv' file per se.",
                                 action = "store_true")
    subparser_args6.add_argument("--metadata",
                                 help = "The csv-formatted metadata file.",
                                 required = True)
    subparser_args6.add_argument("--fasta",
                                 help = "The fasta-formatted nucleotide sequences file.",
                                 required = True)
    subparser_args6.add_argument("--frameshift",
                                 help = "'catch_none': catch none of the frameshifts and release immediately; 'catch_all': catch all frameshifts and require email confirmation; 'catch_novel': catch novel frameshifts and require email confirmation.",
                                 choices = ["catch_all", "catch_novel", "catch_none"],
                                 default = "catch_all",
                                 required = False)
    subparser_args6.add_argument("--failed",
                                 help = "Name of output file to log failed records.",
                                 default = "./failed.out")
    subparser_args7.add_argument("--proxy",
                                 help = "Proxy-configuration for HTTPS-Request in the form: http(s)://username:password@proxy:port.")


    subparser_modules = parser.add_subparsers(
        title="Sub-commands help", help="", metavar="", dest="subparser_name"
    )

    subparser_modules.add_parser(
        "authenticate",
        help="""Write the authentication token.""",
        description="Write the authentication token.",
        parents=[subparser_args1, subparser_args2, subparser_args3, subparser_args7, subparser_args4],
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    subparser_modules.add_parser(
        "upload",
        help="""Upload sequences and metadata.""",
        description="Perform upload of sequences and metadata to GISAID's curation zone.",
        parents=[subparser_args1, subparser_args2, subparser_args6, subparser_args7, subparser_args4],
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    subparser_modules.add_parser("version",
        help = "Show version and exit.")

    subparser_modules.add_parser("template",
        help = "Print template and formatting instructions",
        description="Print to stdout the formatting instructions for the metadata file, or print the 'template.csv' file per se.",
        parents = [subparser_args1, subparser_args5],
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    return parser


def main():
    """The main routine"""
    parser = args_parser()
    args = parser.parse_args()

    if parser.parse_args().subparser_name is None:
        print("usage: cli3 -h")
    elif args.subparser_name == "version":
        from cli3 import __version__
        print(f"cli3 version:{TAB}{__version__}")
    elif args.subparser_name == "template":
        from cli3.utils.instructions import INSTRUCTIONS
        from cli3.utils.colors import Colors
        if not args.template:
            for key, value in INSTRUCTIONS[args.database].items():
                print("")
                print(Colors.RED+key+':')
                print(Colors.BLUE+value+"\n")
        else:
            from cli3.utils.template import TEMPLATE
            print(TEMPLATE)
    else:
        from cli3.handler import handle
        try:
            exit_code, logfile = handle(args)
        except KeyboardInterrupt:
            print("user interrupt")
            sys.exit(1)
        if args.log:
            with open(args.log, "a") as f:
                f.write(json.dumps(logfile, indent = 4))
        get_execution_time()
        sys.exit(exit_code) #no need to do this as python does this implicitly at this stage

if __name__ == "__main__":

    import doctest
    doctest.testmod()
    main()

