__author__ = "Christian Klarhorst"
__copyright__ = "Copyright 2023, Christian Klarhorst"
__email__ = "cklarhor@techfak.uni-bielefeld.de"
__license__ = "MIT"

from snakemake.shell import shell

shell("mkdir -p {snakemake.output[0]} && cd {snakemake.output[0]} && git clone {snakemake.params.git_url} . && git checkout {snakemake.wildcards.git_hash}")