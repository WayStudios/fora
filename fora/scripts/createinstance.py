import optparse
import os
import os.path
import pkg_resources
import sys

class CreateInstanceCommand(object):
    verbosity = 1 #required
    description = 'Render fora scaffolding to an output directory'
    usage = 'usage: %prog [options] -s <scaffold> output_directory'
    parser = optparse.OptionParser(usage, description = description)
    parser.add_option('-s', '--scaffold',
                      dest='scaffold_name',
                      action='append',
                      help=("Add a scaffold to the create process "
                            "(multiple -s args accepted)"))
    parser.add_option('-l', '--list',
                      dest='list',
                      action='store_true',
                      help="List all available scaffold names")
    parser.add_option('--simulate',
                      dest='simulate',
                      action='store_true',
                      help='Simulate but do no work')
    parser.add_option('--overwrite',
                      dest='overwrite',
                      action='store_true',
                      help='Always overwrite')
    parser.add_option('--interactive',
                      dest='interactive',
                      action='store_true',
                      help='When a file would be overwritten, interrogate')

    fora_dist = pkg_resources.get_distribution("fora")

    def __init__(self, argv):
        self.options, self.args = self.parser.parse_args(argv[1:])
        self.scaffolds = self.all_scaffolds()
    def run(self):
        if self.options.list:
            return self.show_scaffolds()
        if not self.options.scaffold_name and not self.args:
            self.parser.print_help()
            self.show_scaffolds()
            return 2
        if not self.options.scaffold_name:
            self.out('You must provide at least one scaffold name: -s <scaffold name>')
            self.show_scaffolds()
            return 2
        if not self.args:
            self.out('You must provide a instance name')
            return 2
        available = [x.name for x in self.scaffolds]
        diff = set(self.options.scaffold_name).difference(available)
        if diff:
            self.out('Unavailable scaffolds: %s' % list(diff))
            return 2
        return self.render_scaffolds()
    def render_scaffolds(self):
        options = self.options
        args = self.args
        output_dir = os.path.abspath(os.path.normpath(args[0]))
        instance_name = os.path.basename(os.path.split(output_dir)[1])

        fora_version = self.fora_dist.version

        vars = {
            'instance': instance_name,
            'fora_version': fora_version,
            'pyramid_docs_branch': 'latest'
        }

        for scaffold_name in options.scaffold_name:
            for scaffold in self.scaffolds:
                if scaffold.name == scaffold_name:
                    scaffold.run(self, output_dir, vars)
        return 0
    def out(self, msg):
        print(msg)
    def show_scaffolds(self):
        scaffolds = sorted(self.scaffolds, key=lambda x: x.name)
        if scaffolds:
            max_name = max([len(t.name) for t in scaffolds])
            self.out('Available scaffolds:')
            for scaffold in scaffolds:
                self.out('  %s:%s  %s' % (
                    scaffold.name,
                    ' ' * (max_name - len(scaffold.name)), scaffold.summary))
        else:
            self.out('No scaffolds available')
        return 0
    def all_scaffolds(self):
        scaffolds = []
        eps = list(pkg_resources.iter_entry_points('fora.scaffold'))
        for entry in eps:
            try:
                scaffold_class = entry.load()
                scaffold = scaffold_class(entry.name)
                scaffolds.append(scaffold)
            except Exception as e: # pragma: no cover
                self.out('Warning: could not load entry point %s (%s: %s)' % (
                    entry.name, e.__class__.__name__, e))
        return scaffolds

def main(argv=sys.argv):
    command = CreateInstanceCommand(argv)
    return command.run()
