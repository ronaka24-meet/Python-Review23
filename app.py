def create_youtube_video(title, description):
    video = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}}
    return video

c = create_youtube_video("ddd", "gg")

print(c)
def like(ytb_vd):
	if "likes" in ytb_vd:
		ytb_vd["likes"] += 1
	return ytb_vd

def dislike(ytb_vd):
	if "dislikes" in ytb_vd:
		ytb_vd["likes"] += 1
	return ytb_vd

def add_comment(ytb_vd, username, comment_text):
    ytb_vd["comments"][username] = comment_text
    return ytb_vd
    
d = add_comment(c, "ff", "gg")
print(d)

for i in range(495):
    like(d)

print(d)