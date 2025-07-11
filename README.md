# ugeeconfig: a command-line Ugee driver XML config editor

This program was developed for the sole purpose of properly configuring my Ugee UE16 tablet, as the ugeeTabletDriver gave me a hard time when dealing with setting the pen buttons, the tablet keys and in general, anything related to keyboard input on GNU/Linux, as for some reason, it wouldn't work properly, sometimes it did, sometimes it did not.\
While I could simply report the problem, I believed that a command-line configurator might have come handy anyway, so I simply decided to make a full program out of this idea.\
It's a shame an official one doesn't exist though.

This program was developed and tested on Debian GNU/Linux testing (Trixie), against the UgeeTabletDriver versions 4.3.4-2411031 and 4.3.5-2411031, available at [https://www.ugee.com/download/ue16](https://www.ugee.com/download/ue16).

For those interested in "how" this software achieves this result, you may take a look at the [documentation file for the Ugee's XML config file](documentation/xml-configfile_documentation.md), in which all my findings are detailed and explained.\
Please note that NO REVERSE ENGINEERING WAS PERFORMED as I'm not an expert on that and above all, I didn't have time for it.

I did a simple "trial and error", I tested the different values by manipulating the XML config file located at `/usr/lib/ugeeTablet/conf/Ugee_Tablet.xml`.\
After doing so, I simply re-run the Ugee Tablet driver multiple times and record the results. It took me a while to figure how most things worked, unfortunately, some things still elude me to this day.

I can't guarantee that the program will work against different driver version's XML config file (e.g. Windows, Mac OS versions) as I focused on the GNU/Linux platform only.


## How to use

Simply clone this repository and execute the program, see "Getting started" for some examples.

```
git clone https://github.com/elluisian/ugeeconfig
cd ugeeconfig
./ugeeconfig.sh <commands>
```

## Dependencies

In order for this program to work properly, you need:

- `Python 3.11`: earlier versions should also work, I cannot guarantee it though;
- The `python3-xlib` module: used to deal with XKeysyms;
- The `python3-lxml` module: used to read/write XML files;
- `bash 5.2`: earlier versions should also work, as long as the BASH\_SOURCE variable is supported;
- The utilities `realpath` and `dirname`: used by the `ugeeconfig.sh` script;

If you also want to check the documentation out, you need:

- Any browser for reading HTMLs or text editors for the Markdown files (.md);
- Any Image viewer for the .png file;
- The `pandoc` utility, since it is used by the `generate-htmls.sh` script located in the documentation directory. Not mandatory;
- The `Dia` utility, since it is used to read .dia file located in the documentation, again, not mandatory;


## Getting started

Most of the operators, commands, names, identifiers and such are treated in a CASE-INSENSITIVE manner. For example, you can refer to the UE16 tablet as "UE16", "ue16", "Ue16" and "uE16", you don't have to memorize the actual case of the letters.


### Getting to know the available props

To check for available properties ("props" from now on), use the `doc` operator:

```
./ugeeconfig.sh doc <prop path>*
```

Below I provided two examples, the first shows all devices plus the deskkeys:

```
./ugeeconfig.sh doc
```

which outputs:

```
RB160: Device data
BP1003W: Device data
[...]
UE16: Device data
deskkeys: Deskkeys data
```

In this second example, we're asking to get the "UE16" and "deskkeys" props only:

```
./ugeeconfig.sh doc UE16 deskkeys
```

with output:

```
UE16: Device data
UE16.pen: Pen data
UE16.tablet: Tablet data
UE16.settings: Settings data
deskkeys: Deskkeys data
deskkeys.fixed: Fixed/movable deskkeys [BOOLEAN]
deskkeys.zoom: Deskkeys window zoom value [FLOAT]
deskkeys.nokeys: Number of virtual keys [INTEGER]
deskkeys.vkey1: Virtual desk key data
deskkeys.vkey2: Virtual desk key data
[...]
deskkeys.vkey16: Virtual desk key data
```

Props are "referrable" through the so-called "prop paths", that is, dot-separated strings which uniquely identify a particular prop (e.g. "UE16.pen.pressure", "deskkeys.zoom", etc).\
As already mentioned, these can be inputted in a CASE-INSENSITIVE manner, each one of these is related to a particular setting of the tablets;

Please note that in order to avoid flooding the screen, the `doc` operator only shows the "direct children" of the specified props.\
In the previous example, by requesting "UE16", the program will show "UE16" and its direct children, that is "UE16.pen", "UE16.tablet" and "UE16.settings", but not "UE16.pen.pressure" which is its grandchildren node.

As can be seen, props are nodes (as in tree/graph teory), so there exist "node props" and "leaf props".\
The first kind simply contains other props, they serve no other purpose but to "establish an order and a hierarchy" (e.g. "UE16" is a node prop, since it contains "pen", "tablet" and "settings"), the second kind contains a value which can be edited, the set of these values, will define the modifications to make to the resultant XML configuration. It is very easy to distinguish the two types as leaf props report their expected type in brackets (e.g. [INTEGER], [FLOAT], etc).\
As a consequence of the above, only leaf props can be modified (with the set operator) and retrieved (with the get operator).



### Getting the props' values

To get the values associated to leaf props, use the `get` operator:

```
./ugeeconfig.sh get <prop path>*
```

The following example gets the values of all the available props:

```
./ugeeconfig.sh get
```

which outputs (be warned, the actual output of this is VERY LONG);

```
[...]
UE16.pen.pressure.enabled: true
UE16.pen.pressure.coords: press(0, 0:0, 1)
UE16.pen.mousemode.enabled: false
UE16.pen.mousemode.speed: 5
UE16.pen.tilt: true
UE16.pen.button0.action_default: FUNCT_ERSR (409)
UE16.pen.button0.action_custom.enabled: false
UE16.pen.button0.action_custom.label: N/A
UE16.pen.button0.action_custom.action: N/A
UE16.pen.button1.action_default: MOUSEK_RCLICK (207)
UE16.pen.button1.action_custom.enabled: false
UE16.pen.button1.action_custom.label: N/A
UE16.pen.button1.action_custom.action: N/A
UE16.pen.button2.action_default: FUNCT_PENERSR (403)
UE16.pen.button2.action_custom.enabled: false
UE16.pen.button2.action_custom.label: N/A
UE16.pen.button2.action_custom.action: N/A
UE16.tablet.key1.action_default: KEYSTRK_B (301)
UE16.tablet.key1.action_custom.enabled: false
UE16.tablet.key1.action_custom.label: N/A
UE16.tablet.key1.action_custom.action: false
UE16.tablet.key2.action_default: KEYSTRK_E (302)
UE16.tablet.key2.action_custom.enabled: false
UE16.tablet.key2.action_custom.label: N/A
UE16.tablet.key2.action_custom.action: N/A
[...]
UE16.tablet.R.wheel_movement1.usage: usg_default
UE16.tablet.R.wheel_movement1.label: N/A
UE16.tablet.R.wheel_movement1.ccw_label: N/A
UE16.tablet.R.wheel_movement1.cw_label: N/A
UE16.tablet.R.wheel_movement1.ccw_action: N/A
UE16.tablet.R.wheel_movement1.cw_action: N/A
UE16.tablet.R.wheel_movement2.usage: usg_default
UE16.tablet.R.wheel_movement2.label: N/A
UE16.tablet.R.wheel_movement2.ccw_label: N/A
UE16.tablet.R.wheel_movement2.cw_label: N/A
UE16.tablet.R.wheel_movement2.ccw_action: N/A
UE16.tablet.R.wheel_movement2.cw_action: N/A
[...]
UE16.tablet.screenres: 1920x1080+0+0
UE16.tablet.tabletres: 1342x755+0+0
UE16.tablet.tabletrot: 0
UE16.settings.messages: true
UE16.settings.tabletkeys: true
deskkeys.fixed: false
deskkeys.zoom: 1.0
deskkeys.nokeys: 4
deskkeys.vkey1.action_default: KEYSTRK_CTRLSHIFTZ (308)
deskkeys.vkey1.action_custom.enabled: false
deskkeys.vkey1.action_custom.label: N/A
deskkeys.vkey1.action_custom.action: N/A
deskkeys.vkey2.action_default: KEYSTRK_CTRLALTZ (307)
deskkeys.vkey2.action_custom.enabled: false
deskkeys.vkey2.action_custom.label: N/A
deskkeys.vkey2.action_custom.action: N/A
[...]
deskkeys.vkey16.action_default: DRV_NOP (10)
deskkeys.vkey16.action_custom.enabled: false
deskkeys.vkey16.action_custom.label: N/A
deskkeys.vkey16.action_custom.action: N/A
```

In this other example, only the values of props contained within the nodes "UE16.pen" and "deskkeys.vkey1" will be shown:

```
./ugeeconfig.sh get UE16.pen deskkeys.vkey1
```

which outputs:

```
UE16.pen.pressure.enabled: true
UE16.pen.pressure.coords: press(0, 0:0, 1)
UE16.pen.mousemode.enabled: false
UE16.pen.mousemode.speed: 5
UE16.pen.tilt: true
UE16.pen.button0.action_default: FUNCT_ERSR (409)
UE16.pen.button0.action_custom.enabled: false
UE16.pen.button0.action_custom.label: N/A
UE16.pen.button0.action_custom.action: N/A
UE16.pen.button1.action_default: MOUSEK_RCLICK (207)
UE16.pen.button1.action_custom.enabled: false
UE16.pen.button1.action_custom.label: N/A
UE16.pen.button1.action_custom.action: N/A
UE16.pen.button2.action_default: FUNCT_PENERSR (403)
UE16.pen.button2.action_custom.enabled: false
UE16.pen.button2.action_custom.label: N/A
UE16.pen.button2.action_custom.action: N/A
deskkeys.vkey1.action_default: KEYSTRK_CTRLSHIFTZ (308)
deskkeys.vkey1.action_custom.enabled: false
deskkeys.vkey1.action_custom.label: N/A
deskkeys.vkey1.action_custom.action: N/A
```

If a prop path is not correct (i.e. does not exist), the program will try to detect possible valid prop paths, basically, acting as a filter, if some prop is found, then they're shown, otherwise, an error is reported.\
The next example illustrates this behaviour:


```
./ugeeconfig.sh get UE16.pen.bu deskkeys.vkey1.action
```

with output:

```
UE16.pen.button0.action_default: FUNCT_ERSR (409)
UE16.pen.button0.action_custom.enabled: false
UE16.pen.button0.action_custom.label: N/A
UE16.pen.button0.action_custom.action: N/A
UE16.pen.button1.action_default: MOUSEK_RCLICK (207)
UE16.pen.button1.action_custom.enabled: false
UE16.pen.button1.action_custom.label: N/A
UE16.pen.button1.action_custom.action: N/A
UE16.pen.button2.action_default: FUNCT_PENERSR (403)
UE16.pen.button2.action_custom.enabled: false
UE16.pen.button2.action_custom.label: N/A
UE16.pen.button2.action_custom.action: N/A
deskkeys.vkey1.action_default: KEYSTRK_CTRLSHIFTZ (308)
deskkeys.vkey1.action_custom.enabled: false
deskkeys.vkey1.action_custom.label: N/A
deskkeys.vkey1.action_custom.action: N/A
```

The `doc` operator behaves similarly.



### Setting the props' values

To edit (leaf) props' values, use the `set` operator:

```
./ugeeconfig.sh set (prop, value)+
```

with `(prop, value)` being a pair composed by a prop path and a value, the two are separated by a space.\
Contrary to previous operators, `set` expects an EVEN number, one prop to set and a value to assign to it.

In the following example, it is requested to edit the UE16 device configuration in order to enable pen pressure and set relative mode's speed to 1:

```
./ugeeconfig.sh set UE16.pen.pressure.enabled t UE16.pen.relmode.speed 1
```

Typical types of values that can be used are:

- Integers (binary, octal, decimal and hexadecimal, see the program's help for details);
- Floats;
- Rectangles with format "rect(x, y, w, h)", with "x", "y", "w", and "h" being integers;
- Pressure points with format "press(p0, p1x, p1y, p2)", with "p0", "p1x", "p1y" and "p2" being numbers (either integers or floats);


Once the editing is completed, the resultant XML config file is printed on screen, it is possible to redirect the output to a file, but it is not the recommended way to solve the problem. More on this later.


#### How to set default actions (actids)

`default_action`'s props can be set using an integer (which represents an actid) or an "actid symbolic name".
The get a list of those, use the `actids` operator:

```
./ugeeconfig.sh actids (keys|mouse|funct|sysop|multim|all)*
```

The names in parentheses can be used to filter what type of actids to show. If nothing is specified or "all" is used, all available actids are shown.\
With the following, only the function-type actids are shown:

```
./ugeeconfig.sh actids funct
```

which outputs:

```
Here follows the actids:

FUNCT_DISPIFACE (401)
FUNCT_SWITCHMON (402)
FUNCT_PENERSR (403)
FUNCT_PRECMODE (404)
FUNCT_SWRING1 (405)
FUNCT_SWRING2 (406)
FUNCT_TRACKMODE (407)
FUNCT_BE (408)
FUNCT_ERSR (409)
FUNCT_DESKKEYS (410)
```

To edit a default action, for example, the one belonging to the button 0 of the UE16's pen, you may use something like this:

```
./ugeeconfig.sh set ue16.pen.button0.action_default funct_deskkeys
```

Please note that the official configuring program does not allow to change the default actions of keys/buttons/etc, but the driver itself supports this.



#### How to set custom actions


Custom actions are a bit tricky in comparison to previous prop types. They are the main reason I developed this program in the first place.\
First of all, any actionable button has an `action_custom` node, each one of these contains the following leaf props:

- `label`: a simple label;
- `enabled`: a flag, if this is set, then the custom action is used;
- `action`: the actual custom action to use;


Please note that, unlike the official configuring program, it is possible to store a custom action (`action` prop) without actually enabling it (`enabled` prop) or without showing any label (`label'` prop).\
In general, you want to set all these props at once, in order to have a complete and well-defined custom action.\
The separation of these properties was done for flexibility reasons;

Custom actions can have only one of the following forms:

- `keys(<keystroke>[,<keystroke>]*)` with`<keystroke>` being in the format `<keysym>[\+<keysym>]*` (keysyms separated by pluses), basically, a list of keystrokes separated by commas;
- `mouse(<mouseactid>[\+<mouseactid>]*)` with `<mouseactid>` being a mouse actid (each one is separated by a plus);
- `exec(<execpath>)` with `<execpath>` being a path to an executable to be run. Please note that command-line parameters are not supported, use custom scripts if needed;
- `funct(<functactid>)` with `<functactid>` being a function actid;
- `sysop(<sysopactid>)` with `<sysopactid>` being a sysop actid (not all of them work on GNU/Linux);
- `multim(<multimactid>)` with `<multimactid>` is a multimedia actid (none of these work on GNU/Linux, they are supported for completeness);
- `unset` or `unset()`, a special custom action that allows to remove a previous defined custom action;
- `nop` or `nop()`, a special custom action that simply states that no action is performed, not even the default one, this is basically "No function set";




#### How to set custom actions for wheel action movements

Wheel movements ("W" tags on the config file) are tough to deal with.\
Each single "wheel action movement" (that's how I decided to call them, I struggled to find a better name, bear with me), has two possible custom actions: a counterclockwise one and a clockwise one.\
Each action can only be of the "keys" type seen above (the one with keystrokes).

Each `"wheel_movement` node contains the following leaf props:

- `usage`: It determines which action is in use, its value can be one of the following keywords:
    - "usg\_default" for using the default action;
    - "usg\_nop" for not using actions, that is, no operation is performed;
    - "usg\_custom" for using the custom action;

- `label`: A label for the wheel action movement in general;
- `ccw_label`: The counterclockwise custom action's label;
- `cw_label`: The clockwise custom action's label;
- `ccw_action`: The counterclockwise (keys) custom action itself;
- `cw_action`: The clockwise (keys) custom action itself;


In the following example, the `wheel_movement4` for the device UE16 is set so that when rotated clockwise, it produces the keystroke `Ctrl_L`.

```
./ugeeconfig.sh set ue16.tablet.r.wheel_movement4.usage usg_custom ue16.tablet.r.wheel_movement4.label "test" ue16.tablet.r.wheel_movement4.cw_action 'keys(ctrl)'
```

Please note that in this case, no action is performed when rotating counterclockwise.



#### X keysyms

Custom actions of the "keys" kind use (in GNU/Linux at least) what is called a "X keysym".\
In X11, X keysyms are used to recognize keyboard input in a layout-independent way, each keysym defines a name for a key and each layout assign xkeysyms differently.\
In fact, different layout may assign different xkeysyms to keys which, among different keyboards with similar appearance, are physically located in the same spot.\
There are many many X keysyms on GNU/Linux, but this program only uses a few of them, provided by the Xlib module.

To show the xkeysyms' symbolic names recognized by the program, use:

```
./ugeeconfig.sh xkeysyms
```

Please note that the output is VERY VERY long, so it might be a good idea to redirect it to a file.

A better way to gather the needed xkeysyms is to use utilities like `xev`, which detects them in real time.\
Please note that in order to properly define working "keys" custom actions, you have to consider not the xkeysym of the produced symbol, but rather, the xkeysyms of the keys that when pressed, produce said symbol.

As an example, consider the left bracket character "[", to get that in American keyboards, you just have to press the corresponding key with xkeysym `bracketleft`, so in this case, the correct custom action is `keys(bracketleft)`.\
If you try to set `keys(bracketleft)` with an Italian keyboard, it won't work, as there's no `bracketleft` key on the keyboard, in that layout in fact, the same physical key uses the `egrave` xkeysym.\
In general, to create the correct custom action, you want to describe the set of keys that are needed to produce `bracketleft` and in the Italian keyboard, you achieve that by using the AltGr and Grave accent E keys.\
Basically, for Italian keyboards, the correct custom action is `keys(altgr+egrave)`.




### Reading and saving configuration files

Up to now, only a few props were shown, edited and documented, but all of this is useless if there is no way to actually make persistent changes.\
Of course this is possible in a neat and clean way, by using the commands "from" and "to".\
In short, "from" indicates to load an existing config file as base for further modifications and "to" establishes where to save the resultant modified config file.

Basically, when "from" is omitted, a default config file is automatically generated by the program and used as a base for the modifications performed by the user. This is good in case you accidentally destroy something important and you want to start over.\
If "to" is omitted, the result is shown on stdout, as already established.

In order to load from a base file and save to another new file, just do the following:

```
./ugeeconfig.sh from <pathsrc> to <pathdest> set <operands>
```

The two paths may be the same, but I personally do not recommend this.\
Here's a very simple example:

```
./ugeeconfig.sh from test.xml to test-edited.xml set ue16.pen.pressure.enabled true
```

Please note that `from` may be used with the `get` operator to get the props' values contained in the specified config file.

Please also note that it is possible to generate a "clean" default XML config file, without any edits.\
To do that, just use the following:

```
./ugeeconfig.sh to <pathdest>
```




## Extra tips (independent of ugeeconfig)

Here follows some additional tips I discovered on my own while using the UE16.
Please note that these are not related to this utility, they are generic usage tips I discovered for myself and that I want to share to improve your experience.



### Keystrokes keys recognized as other totally diferent keys

Be sure your keyboard layout is properly set.
It happened to me that, standard applications worked correctly with my layout, but the driver didn't recognize it properly, for some weird reason in fact, it required `bracketright` to zoom in GIMP, despite my earlier discussion on layouts!

If you use input managers like `ibus` you should be fine, as it handles this problem in a neat way.
If you do not use these and do not intend to, you can check your current keymap with the following command:

```
setxkbmap -query
```

If it does not correspond, then force it with:

```
setxkbmap it # change according to your particular locale
```



### Messages remove focus from windows in IceWM

If IceWM is not properly configured, the messages window removes the focus from the program you're working on (e.g. GIMP), removing, this way, any possibility of interaction with said program.

To fix this, add the following to the `winoptions` config file:

```
ugeeTablet.ugeeTablet.layer: AboveAll
ugeeTablet.ugeeTablet.doNotFocus: 1
```

and restart IceWM.