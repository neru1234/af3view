from pymol import cmd
import argparse
import os


def parserun(inputf, name, outputf, pngfile=None, first='A', second='B', resrange=5, label=False, transparency=0.6):
    cmd.load(inputf)
    cmd.select("chainA", f"chain {first}") 
    cmd.select("chainB", f"chain {second}")
    cmd.create("aa", "chainA")
    cmd.create("bb", "chainB")
    cmd.delete("chainA")
    cmd.delete("chainB")
    cmd.delete(name)
    cmd.color_deep("green", "aa", 0)
    cmd.color_deep("cyan", "bb", 0)
    cmd.set("bg_rgb", [1, 1, 1])
    cmd.set("cartoon_transparency", transparency)
    cmd.select("nearby_aa_residues", f"byres aa within {resrange} of bb")
    cmd.create("aa_residues", "nearby_aa_residues") 
    cmd.select("nearby_bb_residues", f"byres bb within {resrange} of aa")
    cmd.create("bb_residues", "nearby_bb_residues")
    cmd.color_deep("splitpea", "aa_residues", 0)
    cmd.color_deep("teal", "bb_residues", 0)
    cmd.delete("nearby_aa_residues")
    cmd.delete("nearby_bb_residues")
    cmd.dist("polar_contacts", "aa", "bb", mode=2, label=0)
    cmd.color_deep("red", "polar_contacts", 0)
    cmd.show("sticks", "aa_residues")
    cmd.show("sticks", "bb_residues")
    cmd.hide("sticks","aa")
    cmd.hide("sticks","bb")
    if label:
        cmd.label('''byca(aa_residues)''', 'oneletter+resi')
        cmd.label('''byca(bb_residues)''', 'oneletter+resi')
    cmd.save(outputf)
    if pngfile:
        cmd.refresh()
        bounding_box = cmd.get_extent("all")
        x_min, y_min, z_min = bounding_box[0]
        x_max, y_max, z_max = bounding_box[1]
        width = int((x_max - x_min) * 100)
        height = int((y_max - y_min) * 100)
        cmd.png(pngfile, width=width, height=height, dpi=300, ray=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='parseaf3.py --input xxx.cif [--first a] [--second b] [--lable 1] [--output xxx.pse]')
    parser.add_argument('--input', metavar='<file path>', help='model file cif or pdb')
    parser.add_argument('--first', metavar='<first chain>', default='a', help='the first chain')
    parser.add_argument('--second', metavar='<second chain>', default='b', help='the second chain')
    parser.add_argument('--label', metavar='1|0', default='0', help='1: label all residues;0: no labels for all')
    parser.add_argument('--output', metavar='<file path>', default='', help='pse output file')
    parser.add_argument('--range', metavar='<rang>', default=5, help='rang for residue view with unit Å')
    args = parser.parse_args()
    if args.input.endswith('cif') or args.input.endswith('pdb'):
        inputf = args.input
        name = os.path.basename(inputf).split(r'.')[0]
    else:
        raise Exception('Please input full cif or pdb file path')
    first = args.first.upper()
    second = args.second.upper()
    if args.label == '1':
        label = True
    else:
        label = False
    if args.output and args.output.endswith('pse'):
        outputf = args.output
        pngfile = '.'.join(args.output.split(r'.')[0], 'png')
    else:
        outputf = os.path.join(args.output, f'{name}.pse')
        pngfile = os.path.join(args.output, f'{name}.png')
    resrange = int(args.range)
    parserun(inputf=inputf, name=name, outputf=outputf, pngfile=False, first=first, second=second, resrange=resrange, label=label)
    print(f'This pse file is: {outputf}')

