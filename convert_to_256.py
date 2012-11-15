# converts a vim color file from gui to terminal 256 color
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
            outfile.write("\" Sets correct colors\n")
            outfile.write("silent ! echo -n '")
            for color, code in color_map.iteritems():
                outfile.write("\\033]4;%s;rgb:%s/%s/%s\\033 " % (code, color[0:2], color[2:4], color[4:6]))
            outfile.write("'\nredraw!\n")
            outfile.write("\" End setting\n")
            outfile.write("let &t_te='\033]4;216;rgb:ff/af/87\033 \033]4;217;rgb:ff/af/af\033 \033]4;214;rgb:ff/af/00\033 \033]4;215;rgb:ff/af/5f\033 \033]4;212;rgb:ff/87/df\033 \033]4;213;rgb:ff/87/ff\033 \033]4;210;rgb:ff/87/87\033 \033]4;211;rgb:ff/87/af\033 \033]4;165;rgb:df/00/ff\033 \033]4;218;rgb:ff/af/df\033 \033]4;219;rgb:ff/af/ff\033 \033]4;133;rgb:af/5f/af\033 \033]4;132;rgb:af/5f/87\033 \033]4;131;rgb:af/5f/5f\033 \033]4;130;rgb:af/5f/00\033 \033]4;137;rgb:af/87/5f\033 \033]4;136;rgb:af/87/00\033 \033]4;135;rgb:af/5f/ff\033 \033]4;134;rgb:af/5f/df\033 \033]4;139;rgb:af/87/af\033 \033]4;138;rgb:af/87/87\033 \033]4;166;rgb:df/5f/00\033 \033]4;24;rgb:00/5f/87\033 \033]4;25;rgb:00/5f/af\033 \033]4;26;rgb:00/5f/df\033 \033]4;27;rgb:00/5f/ff\033 \033]4;20;rgb:00/00/df\033 \033]4;21;rgb:00/00/ff\033 \033]4;22;rgb:00/5f/00\033 \033]4;23;rgb:00/5f/5f\033 \033]4;160;rgb:df/00/00\033 \033]4;28;rgb:00/87/00\033 \033]4;29;rgb:00/87/5f\033 \033]4;161;rgb:df/00/5f\033 \033]4;163;rgb:df/00/af\033 \033]4;119;rgb:87/ff/5f\033 \033]4;120;rgb:87/ff/87\033 \033]4;121;rgb:87/ff/af\033 \033]4;122;rgb:87/ff/df\033 \033]4;123;rgb:87/ff/ff\033 \033]4;124;rgb:af/00/00\033 \033]4;125;rgb:af/00/5f\033 \033]4;126;rgb:af/00/87\033 \033]4;127;rgb:af/00/af\033 \033]4;128;rgb:af/00/df\033 \033]4;129;rgb:af/00/ff\033 \033]4;167;rgb:df/5f/5f\033 \033]4;118;rgb:87/ff/00\033 \033]4;59;rgb:5f/5f/5f\033 \033]4;58;rgb:5f/5f/00\033 \033]4;55;rgb:5f/00/af\033 \033]4;54;rgb:5f/00/87\033 \033]4;57;rgb:5f/00/ff\033 \033]4;56;rgb:5f/00/df\033 \033]4;51;rgb:00/ff/ff\033 \033]4;50;rgb:00/ff/df\033 \033]4;53;rgb:5f/00/5f\033 \033]4;52;rgb:5f/00/00\033 \033]4;164;rgb:df/00/df\033 \033]4;201;rgb:ff/00/ff\033 \033]4;199;rgb:ff/00/af\033 \033]4;179;rgb:df/af/5f\033 \033]4;200;rgb:ff/00/df\033 \033]4;195;rgb:df/ff/ff\033 \033]4;194;rgb:df/ff/df\033 \033]4;197;rgb:ff/00/5f\033 \033]4;178;rgb:df/af/00\033 \033]4;191;rgb:df/ff/5f\033 \033]4;190;rgb:df/ff/00\033 \033]4;193;rgb:df/ff/af\033 \033]4;192;rgb:df/ff/87\033 \033]4;115;rgb:87/df/af\033 \033]4;114;rgb:87/df/87\033 \033]4;88;rgb:87/00/00\033 \033]4;89;rgb:87/00/5f\033 \033]4;111;rgb:87/af/ff\033 \033]4;110;rgb:87/af/df\033 \033]4;113;rgb:87/df/5f\033 \033]4;112;rgb:87/df/00\033 \033]4;82;rgb:5f/ff/00\033 \033]4;83;rgb:5f/ff/5f\033 \033]4;80;rgb:5f/df/df\033 \033]4;81;rgb:5f/df/ff\033 \033]4;86;rgb:5f/ff/df\033 \033]4;87;rgb:5f/ff/ff\033 \033]4;84;rgb:5f/ff/87\033 \033]4;85;rgb:5f/ff/af\033 \033]4;251;rgb:c6/c6/c6\033 \033]4;198;rgb:ff/00/87\033 \033]4;206;rgb:ff/5f/df\033 \033]4;226;rgb:ff/ff/00\033 \033]4;177;rgb:df/87/ff\033 \033]4;254;rgb:e4/e4/e4\033 \033]4;247;rgb:9e/9e/9e\033 \033]4;255;rgb:ee/ee/ee\033 \033]4;225;rgb:ff/df/ff\033 \033]4;245;rgb:8a/8a/8a\033 \033]4;244;rgb:80/80/80\033 \033]4;108;rgb:87/af/87\033 \033]4;109;rgb:87/af/af\033 \033]4;241;rgb:60/60/60\033 \033]4;240;rgb:58/58/58\033 \033]4;243;rgb:76/76/76\033 \033]4;242;rgb:66/66/66\033 \033]4;102;rgb:87/87/87\033 \033]4;103;rgb:87/87/af\033 \033]4;100;rgb:87/87/00\033 \033]4;101;rgb:87/87/5f\033 \033]4;106;rgb:87/af/00\033 \033]4;107;rgb:87/af/5f\033 \033]4;104;rgb:87/87/df\033 \033]4;105;rgb:87/87/ff\033 \033]4;39;rgb:00/af/ff\033 \033]4;38;rgb:00/af/df\033 \033]4;33;rgb:00/87/ff\033 \033]4;32;rgb:00/87/df\033 \033]4;31;rgb:00/87/af\033 \033]4;30;rgb:00/87/87\033 \033]4;37;rgb:00/af/af\033 \033]4;36;rgb:00/af/87\033 \033]4;35;rgb:00/af/5f\033 \033]4;34;rgb:00/af/00\033 \033]4;246;rgb:94/94/94\033 \033]4;252;rgb:d0/d0/d0\033 \033]4;205;rgb:ff/5f/af\033 \033]4;223;rgb:ff/df/af\033 \033]4;176;rgb:df/87/df\033 \033]4;60;rgb:5f/5f/87\033 \033]4;61;rgb:5f/5f/af\033 \033]4;62;rgb:5f/5f/df\033 \033]4;63;rgb:5f/5f/ff\033 \033]4;64;rgb:5f/87/00\033 \033]4;65;rgb:5f/87/5f\033 \033]4;66;rgb:5f/87/87\033 \033]4;67;rgb:5f/87/af\033 \033]4;68;rgb:5f/87/df\033 \033]4;69;rgb:5f/87/ff\033 \033]4;175;rgb:df/87/af\033 \033]4;174;rgb:df/87/87\033 \033]4;173;rgb:df/87/5f\033 \033]4;172;rgb:df/87/00\033 \033]4;171;rgb:df/5f/ff\033 \033]4;170;rgb:df/5f/df\033 \033]4;203;rgb:ff/5f/5f\033 \033]4;222;rgb:ff/df/87\033 \033]4;181;rgb:df/af/af\033 \033]4;253;rgb:da/da/da\033 \033]4;248;rgb:a8/a8/a8\033 \033]4;182;rgb:df/af/df\033 \033]4;183;rgb:df/af/ff\033 \033]4;180;rgb:df/af/87\033 \033]4;162;rgb:df/00/87\033 \033]4;187;rgb:df/df/af\033 \033]4;184;rgb:df/df/00\033 \033]4;220;rgb:ff/df/00\033 \033]4;186;rgb:df/df/87\033 \033]4;188;rgb:df/df/df\033 \033]4;189;rgb:df/df/ff\033 \033]4;202;rgb:ff/5f/00\033 \033]4;196;rgb:ff/00/00\033 \033]4;221;rgb:ff/df/5f\033 \033]4;185;rgb:df/df/5f\033 \033]4;99;rgb:87/5f/ff\033 \033]4;98;rgb:87/5f/df\033 \033]4;168;rgb:df/5f/87\033 \033]4;169;rgb:df/5f/af\033 \033]4;229;rgb:ff/ff/af\033 \033]4;228;rgb:ff/ff/87\033 \033]4;91;rgb:87/00/af\033 \033]4;90;rgb:87/00/87\033 \033]4;93;rgb:87/00/ff\033 \033]4;92;rgb:87/00/df\033 \033]4;95;rgb:87/5f/5f\033 \033]4;94;rgb:87/5f/00\033 \033]4;97;rgb:87/5f/af\033 \033]4;96;rgb:87/5f/87\033 \033]4;17;rgb:00/00/5f\033 \033]4;16;rgb:00/00/00\033 \033]4;19;rgb:00/00/af\033 \033]4;18;rgb:00/00/87\033 \033]4;117;rgb:87/df/ff\033 \033]4;250;rgb:bc/bc/bc\033 \033]4;116;rgb:87/df/df\033 \033]4;204;rgb:ff/5f/87\033 \033]4;151;rgb:af/df/af\033 \033]4;150;rgb:af/df/87\033 \033]4;153;rgb:af/df/ff\033 \033]4;152;rgb:af/df/df\033 \033]4;155;rgb:af/ff/5f\033 \033]4;154;rgb:af/ff/00\033 \033]4;157;rgb:af/ff/af\033 \033]4;156;rgb:af/ff/87\033 \033]4;159;rgb:af/ff/ff\033 \033]4;158;rgb:af/ff/df\033 \033]4;234;rgb:1c/1c/1c\033 \033]4;238;rgb:44/44/44\033 \033]4;239;rgb:4e/4e/4e\033 \033]4;207;rgb:ff/5f/ff\033 \033]4;235;rgb:26/26/26\033 \033]4;236;rgb:30/30/30\033 \033]4;237;rgb:3a/3a/3a\033 \033]4;230;rgb:ff/ff/df\033 \033]4;231;rgb:ff/ff/ff\033 \033]4;232;rgb:08/08/08\033 \033]4;233;rgb:12/12/12\033 \033]4;224;rgb:ff/df/df\033 \033]4;48;rgb:00/ff/87\033 \033]4;49;rgb:00/ff/af\033 \033]4;46;rgb:00/ff/00\033 \033]4;47;rgb:00/ff/5f\033 \033]4;44;rgb:00/df/df\033 \033]4;45;rgb:00/df/ff\033 \033]4;42;rgb:00/df/87\033 \033]4;43;rgb:00/df/af\033 \033]4;40;rgb:00/df/00\033 \033]4;41;rgb:00/df/5f\033 \033]4;146;rgb:af/af/df\033 \033]4;147;rgb:af/af/ff\033 \033]4;144;rgb:af/af/87\033 \033]4;145;rgb:af/af/af\033 \033]4;142;rgb:af/af/00\033 \033]4;143;rgb:af/af/5f\033 \033]4;140;rgb:af/87/df\033 \033]4;141;rgb:af/87/ff\033 \033]4;209;rgb:ff/87/5f\033 \033]4;208;rgb:ff/87/00\033 \033]4;148;rgb:af/df/00\033 \033]4;149;rgb:af/df/5f\033 \033]4;77;rgb:5f/df/5f\033 \033]4;76;rgb:5f/df/00\033 \033]4;75;rgb:5f/af/ff\033 \033]4;74;rgb:5f/af/df\033 \033]4;73;rgb:5f/af/af\033 \033]4;72;rgb:5f/af/87\033 \033]4;71;rgb:5f/af/5f\033 \033]4;70;rgb:5f/af/00\033 \033]4;79;rgb:5f/df/af\033 \033]4;78;rgb:5f/df/87\033 \033]4;249;rgb:b2/b2/b2\033 \033]4;227;rgb:ff/ff/5f\033'.&t_te\n")
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
