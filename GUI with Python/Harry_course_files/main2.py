import tkinter

root = tkinter.Tk()

root.title("LivVyas")

# Important Label() Attributes

# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = tkinter.Label(text='''
Abdul Rashid Salim Salman Khan is an Indian 
\nfilm actor, producer, occasional playback singer and television personality. In a film career spanning 
\nalmost thirty years, Khan has received numerous awards, including two National Film Awards as a film 
\nproducer, and two Filmfare Awards for acting. He has a significant following in Asia and the Indian 
\ndiaspora worldwide, and is cited in the media as one of the most commercially successful actors of Indian 
\ncinema. According to the Forbes 2018 list of Top-Paid 100 Celebrity Entertainers in world, Khan was 
\nthe highest ranked Indian with 82nd rank with earnings of $37.7 million.''',
                            bg='red', fg='white', padx=5, pady=20, font='calibri 9 bold italic', borderwidth=5,
                            relief='sunken')

# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side="bottom", anchor='se', fill='x')
title_label.pack(side="left", anchor='se', fill='y')

root.mainloop()
