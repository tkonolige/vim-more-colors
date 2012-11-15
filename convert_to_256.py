# converts a vim color file from gui to terminal 256 color
# \033]4;105;rgb:ff/ff/00
# set t_AF=<ESC>[38;5%dm
import sys, re

def hex_to_ascii(color):
    ''' convert a hex color to the closest ascii color code '''
    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)
    rn, gn, bn = map(lambda x: round(x/51.0), [r, g, b])
    return str(16 + int(bn) + int(gn*6) + int(rn*36))

def hex_to_ascii2(color):
    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)
    return str(r+256*g+256*256*b)

def file_to_256(i):
    with open(i) as infile:
        new_name = i
        i = new_name.rfind(".")
        new_name = new_name[:i] + "-256" + new_name[i:] 
        with open(new_name, "w") as outfile:
            for line in infile:
                line = line.replace("gui", "cterm") # color terminal, not gui
                line = re.sub(r"#([0-9a-fA-F]{6})", lambda x: hex_to_ascii(x.group(1)), line)
                outfile.write(line)
            
def file_to_more_colors(i):
    with open(i) as infile:
        colors = set()
        for line in infile:
            matches = re.findall(r"(?<=#)[0-9a-fA-F]{6}", line)
            for x in matches:
                colors.add(x)
        color_map = dict(zip(colors, map(lambda s: str(s), range(16, 255-16))))
        with open(re.sub('\.[^\.]*$', lambda x: '-more'+x.group(0), i), 'w') as outfile:
            infile.seek(0)
            outfile.write("silent ! echo '")
            for color, code in color_map.iteritems():
                outfile.write("\\033]4;%s;rgb:%s/%s/%s\\033 " % (code, color[0:2], color[2:4], color[4:6]))
            outfile.write("'\nredraw!\n")
            for line in infile:
                line = line.replace("gui", "cterm")
                line = re.sub(r"#([0-9a-fA-F]{6})", lambda x: color_map[x.group(1)], line)
                outfile.write(line)

def color_print(s, c):
    print "\033[38;5;%sm%s\033[0m" % (hex_to_ascii(c), s)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print "Usage %s: colorscheme.vim" % sys.argv[0]
        sys.exit(1)
    
    file_to_256(sys.argv[1])
    file_to_more_colors(sys.argv[1])
