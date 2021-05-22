import argparse
import subprocess
from utils import schema_generator

parser = argparse.ArgumentParser()

# UTILITY PARSER
## Schema generator
sub_parser = parser.add_subparsers(title="Options")
parser_utils = sub_parser.add_parser("generate-schema", help="generate gql schema (SDL & introspections)")
parser_utils.set_defaults(func=schema_generator.generate)
## test
parser_test = sub_parser.add_parser("test", help="test this project")
parser_test.set_defaults(func=lambda x: subprocess.run(["python", "-m", "unittest", "discover"]))



# google parser example
# compute = parser_utils.add_subparsers(title="Compute Engine")
# compute_parser = sub_parser.add_parser("compute", help="compute engine utility")
# compute_parser.set_defaults(func=lambda x: print("compute engine utility"))

# compute_instances = compute_parser.add_subparsers(title="Options")
# compute_instances_parser = compute_instances.add_parser("instances", help="crud instances")
# compute_instances_parser.set_defaults(func=lambda x: print("compute engine instances crud, size: ", x.disk_size))
# compute_instances_parser.add_argument("--disk-size", default="200GB")

# compute_instances_options = compute_instances_parser.add_subparsers(title="Options")
# compute_instances_create_parser = compute_instances_options.add_parser("create", help="create instance")
# compute_instances_create_parser.set_defaults(func=lambda x: print("create instance"))
# compute_instances_list_parser = compute_instances_options.add_parser("list", help="list instances")
# compute_instances_list_parser.set_defaults(func=lambda x: print("list instance"))
# compute_instances_update_parser = compute_instances_options.add_parser("update", help="update instance")
# compute_instances_update_parser.set_defaults(func=lambda x: print("update instance"))
# compute_instances_delete_parser = compute_instances_options.add_parser("delete", help="delete instance")
# compute_instances_delete_parser.set_defaults(func=lambda x: print("delete instance"))
# compute_instances_get_parser = compute_instances_options.add_parser("get", help="get instance")
# compute_instances_get_parser.set_defaults(func=lambda x: print("get instance"))
