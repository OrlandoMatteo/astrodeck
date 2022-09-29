import os
import sys

import frontmatter


def splitMD(raw, filename):
    slides = raw.content.split('---')
    dir = 'src/pages/'+filename
    try:
        os.mkdir(dir)
    except Exception as e:
        print(e)

    for i, slide in enumerate(slides):
        # save slide in md file
        raw.metadata["nextPage"] = str(i+1).zfill(2)
        p = frontmatter.Post(slide, **raw.metadata)
        toWrite = frontmatter.dumps(p)
        with open(dir+'/'+str(i).zfill(2)+'.md', 'w') as fp:
            fp.write(toWrite)

def createSlide(filename):
    raw = frontmatter.load(open('src/slides/'+filename+'.md'))
    splitMD(raw, filename)


if __name__ == "__main__":
    createSlide(sys.argv[1])
