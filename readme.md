https://tkdocs.com/tutorial/styles.html
https://github.com/TomSchimansky/CustomTkinter

neue class um gui elemente darzustellen
btn1 = class(var1,var2, ...)
efficiency

13.02.2022
    clean class functions for initialize materials
    done with container boxes
        included progressbar
        and editable values
    button started
        cant print text in front of label background button

14.02.2022
    cleaned up functions with syntax
    set region for ui script
    new library for buttons and others

27.02.2022
    actived supply window needs to refresh after beeing in settings and changed
    variables are declared but cant access them, because of circulating

08.03.2022
    delete in ui_toplevel 2 sliderfunction and use only 1

09.03.2022
    ui_toplevel
        added result bar at bottom
        slider can now be set to 0 and wont move when deactivated | draw()

12.03.2022
    new ui design | blue
    optimized positionings of all containers
    Resultsize calculations
        setup increase and decrease buttons
        disable buttons when supply was turned off
        max. and min. of amount
        resets container result value when changing portion size

    mid:
    commented container config

13.03.2022
    sorted scripts into files
    so optimizations

14.03.2022
    test new keyboard on rpi
    # https://raspberrypi.stackexchange.com/questions/81681/virtual-on-screen-keyboard-for-raspberry-pi-touch-screen
    # https://thepihut.com/blogs/raspberry-pi-tutorials/matchbox-keyboard-raspberry-pi-touchscreen-keyboard

    new ui_settings and ui_input files | toplevels
    function to read current container values and names
    function to write values of input entry to config
    new toplevel designs

git init
git remote add origin https://github.com/Saschax99/Muesli-Master.git
git add "" or git add . for everything
git commit -m "first commit 09.03.2022" ex.
git status was verändert wurde
git push

every element definieren mit ex. # ENTRY KCAL

Portionsgröße entfernen -> Portionsmenge angeben: 6 Löffel mit x Gramm
Checkboxen entfernen -> Wenn behälter Leer dann Buttons deaktiviert