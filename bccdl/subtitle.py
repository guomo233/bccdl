import json

ass_head = """[Script Info]
Title: xxx
ScriptType: v4.00+
WrapStyle: 2
ScaledBorderAndShadow: yes
PlayResX: 1280
PlayResY: 720
YCbCr Matrix: TV.709

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,華康中圓體(P),40,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,0,2,10,10,15,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Comment: 0,0:00:00.00,0:00:00.00,Default,,0,0,0,,Staff
Comment: 0,0:00:00.00,0:00:00.00,Default,,0,0,0,,Text"""

ass_end = 'Comment: 0,0:00:00.00,0:00:00.00,Default,,0,0,0,,'

def sec2time(sec):
	h = int(sec) // 3600
	m = int(sec) // 60 % 60
	s = sec % 60
	f = int(sec * 1000) % 1000
	return "%d:%02d:%02d.%02d" % (h, m, s, f // 10)
	
def bcc2ass(bcc, ass_path):
	bcc = json.loads(bcc)
	with open (ass_path, 'w') as ass_f:
		ass_f.write (ass_head)
		for sub in bcc['body']:
			ass_f.write ('Dialogue: 0,%s,%s,Default,,0,0,0,,%s\n' % 
				(sec2time(sub['from']), sec2time(sub['to']), sub['content'].replace('\n', '\\n')))
		ass_f.write (ass_end)
