#!/usr/bin/python3

import os, sys, argparse, subprocess
from TestRunner import TestRunner

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    testing= parser.add_argument_group('testing', '')
    testing.add_argument("--loss", type=int, nargs='+', help="run loss tests for given values [%%]")
    testing.add_argument("--delay", type=int, nargs='+', help="run delay tests for given values [ms]")
    testing.add_argument("--limit", type=int, nargs='+', help="run limit tests for given values [kbit]")
    testing.add_argument("--duplication", type=int, nargs='+', help="run duplication tests for given values [%%]")
    testing.add_argument("--corruption", type=int, nargs='+', help="run corruption tests for given values [%%]")
    testing.add_argument("--reorder", type=int, nargs='+', help="run reorder tests for given values [%%]")
    testing.add_argument("--scalability", type=int, nargs='+', help="number of subscribing nodes")
    testing.add_argument("--test", choices=TestRunner.tests, nargs='+', help="Transport layer to be tested")
    testing.add_argument("--skip-execution", action='store_true', help="parse and plot existing data")
    testing.add_argument("--calculate-mean", action='store_true', help="find all previous results and calculate mean values")
    testing.add_argument("--test-id", help="store this test id with results for later reference")
    tools = parser.add_argument_group('tools', '')
    tools.add_argument("--build-all", action='store_true', help ="build all images")
    tools.add_argument("--build", choices=TestRunner.images, nargs='+', help="delete an existing image and build a new one")
    tools.add_argument("--clean", action='store_true', help ="stop and remove all containers")
    tools.add_argument("--qtcreator", help="Run QT Creator in the specified image")
    if not os.path.isdir("comm"):
        print("Run this script from the project root directory, e.g.: ./python/run.py")
    elif len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        runner = TestRunner()
        if args.build:
            for image in reversed(args.build):
                runner.remove_containers(image)
                subprocess.call("./scripts/remove_image.sh {}".format(image), shell = True)
            for image in args.build:
                subprocess.call("./scripts/build_image.sh {}".format(image), shell = True)
        elif args.build_all:
            for name in reversed(runner.images):
                runner.remove_containers(name)
                subprocess.call("./scripts/remove_image.sh {}".format(name), shell = True)
            for name in runner.images:
                subprocess.call("./scripts/build_image.sh {}".format(name), shell = True)
        elif args.qtcreator:
            subprocess.call("./scripts/qtcreator.sh {} {}".format(args.qtcreator, os.getcwd()), shell = True)
        elif args.clean:
            for name in runner.images:
                runner.remove_containers(name)
        else:
            if not os.geteuid() == 0:
                sys.exit("Only root can run tests")
            if not args.skip_execution:
                runner.dirs(args.test_id)
            for comm in args.test:
                if args.limit:
                    runner.limit(comm, args.limit, args.skip_execution, args.calculate_mean)
                if args.loss:
                    runner.loss(comm, args.loss, args.skip_execution, args.calculate_mean)
                if args.delay:
                    runner.delay(comm, args.delay, args.skip_execution, args.calculate_mean)
                if args.corruption:
                    runner.corruption(comm, args.corruption, args.skip_execution, args.calculate_mean)
                if args.duplication:
                    runner.duplication(comm, args.duplication, args.skip_execution, args.calculate_mean)
                if args.reorder:
                    runner.reorder(comm, args.reorder, args.skip_execution, args.calculate_mean)
                if args.scalability:
                    runner.scalability(comm, args.scalability, args.skip_execution, args.calculate_mean)
                runner.kill()
