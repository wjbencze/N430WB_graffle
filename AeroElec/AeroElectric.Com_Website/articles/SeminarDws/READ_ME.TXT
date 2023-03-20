                        Here's what you have . . . .

drawings.zip

There are 4 foldout drawings (Foldout(x).dwg) intended to be plotted
11 x 17 or as two 8-1/2 x 11 and taped together, which are similar to
Figures in the back of the AeroElectric Connection.

There's a wirebook.dwg file which will provide the beginning for a
custom wire book to be printed on 8-1/2 x 11 pages.

All remaining drawings represent a large portion of a symbols library
used on the foldout drawings and the wirebook.  One file (symbols.dwg)
is a single file which contains a number of commonly used symbols which
can be imported into your drawing(s) in one stroke. 

Most of the other .dwg files are individual symbols and/or pieces of
drawings that I've found very useful over the years.

There are two AutoCAD .shx files . . . romans.shx and velvet_l.shx.  These
are the only two fonts I used on the drawings . .  not everyone has these
in their AutoCAD support library so I've included them here.

                        What you don't have . . . 

No drawing contained on this disk is offered as a correct or complete way
to do any given task.  I used these drawings as starting points to develop
custom diagrams for clients.  These files are offered free of charge, as
is, to assist individuals in developing their own wiring diagrams and/or
wire books.

                         What to do first . . . 

I'd suggest that you copy symbols.dwg, foldouts.dwg and wirebook.dwg to
your hard disk and open them one at a time.  Ask AutoCAD to display BLOCKS.
Survey all of the drawings for titles of blocks and make a list. Obviously,
some of the blocks you will find incorporated into drawings will duplicate
individual drawing files supplied as insertable blocks but the drawings
may include symbols that are used nowhere else.  Write individual blocks
(writeblock) out to the hard drive. When all blocks are represented by
individual files on your harddrive, copy the remaining blocks into the
same directory and add them to your written list.

Now, make a new drawing that contains a number of 8-1/2 x 11 pages (you
could start with wirebook.dwg and erase all it's contents leaving only
the borders and views).  Import each symbol into the new drawing and
place it on a page in a convenient location and TEXT it's name adjacent
to the item.  The task is to build a catalog of symbols. I don't have
one because I've been using these things so long I can generally spot
what I need from a simple list of files.  A printed catalog of symbols
will be quite useful to a new user.

                   Some tips on using existing drawings . . .

(1) I've drawn most of the symbols to fit wires spaced at integer increments
of 0.15"

(2) Views in the wirebook.dwg are on a 12" by 9" matrix. When you restore
any view (1 through 30) you will get exactly the image that will print on
a h-p laserjet printer.  Note tiny circles in the upper left and lower right
corners of each view. Centers of these circles represent opposite corners of
the view. They are positioned to prevent the printer driver from deleting
a border edge at print time . .  they also provide some whitespace at the
left edge for 3-hole punching the sheet.

(3) The wirebook.dwg has a block called BORDER that incorporates a standard
border with mini-titleblock, limit circles and a view number in the upper
right hand corner.  I've found it most inconvenient to attempt any sort
of "order" on the wirebook drawing. I just stick a drawing into any slot
that's empty or add slots to the right taking care to maintain the 12x9
matrix (you can the move large chunks of image from on view to another
by calling out a base 0,0 offsetting by 12k,9j).  The only "order" on the
drawing is to keep the viewnumber (V1, V2, . . .etc) in agreement with the
drawing view.  When your wirebook is printed, you can quickly get back to
any page desired by calling the view as described in the upper right corner
of each page.

(4) There is a script file (plotfile.scr) that can be edited as needed to
add viewplot callouts . . . you won't need to delete any, the AutoCAD
doesn't crash when you ask it to plot a view that doesn't exist. I've
set up the script file to print all views to disk as plot files (make sure
AutoCAD is set up to output HPGL/2 or whatever language is appropriate to
your printer).  Also make sure you're set up to plot views to file
names.

I've found that some printers are too slow and AutoCAD will time
out when trying to print a succession of 30 views to a slow 
printer.  By printing them out to disk, you can use two DOS commands to
print your book without a hitch. First, say "MODE LPT1: RETRY=P"  This
command will keep DOS from timing out during a long printout.  Then
say "COPY *.PLT LPT1:"  This will prompt DOS to print your complete
wirebook while you go watch TV.

                       Final note . . . .
                       
I am pleased to supply these files to assist builders who have access to
resources required to utilize what they contain. However, this will be
a "learning experience" for anyone who does not have extensive skills with
AutoCAD. Please feel free to contact me with any questions on small points
of utilization but understand that my business is the marketing of my
time and talents; I'm not in a position to offer gratis tutorial assistance
in AutoCAD basics.

    Bob Nuckolls
    AeroElectric Connection
    6936 Bainbridge Road
    Wichita, KS  67226-1008
    Phone (316) 685-8617
    E-Mail http://www.aeroelectric.com/bob.nuckolls   