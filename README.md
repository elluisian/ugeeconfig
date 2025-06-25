# UgeeConfig: a commandline Ugee driver configurator

This program was developed for the sole purpose of properly configuring my Ugee UE16 tablet, as the ugeeTabletDriver gave me a hard time when dealing with setting the pen buttons, the tablet keys and in general, anything related to keyboard input on GNU/Linux, as for some reason, it wouldn't work properly, sometimes it did, sometimes it did not.
While I could simply report the problem, I think a command-line configurator may come handy anyway, so I simply decided to make a full program out of this idea, it's a shame it doesn't exist an official one.

The program was developed and tested on Debian GNU/Linux testing (Trixie), with driver version 4.3.4/4.3.5-2411031 available at [https://www.ugee.com/download/ue16](https://www.ugee.com/download/ue16).

For those interested in the "how" this program accomplishes this, you may take a look at the file [xml\_configfile\_documentation.md](documentation/xml_configfile_documnetation.md), which explains all my findings in relation to how the driver uses and treats its XML config file.

Please note that NO REVERSE ENGINEERING WAS PERFORMED as:

- I'm not expert;
- I did not have time for that;

I did a simple "trial and error", I tested the different values by manipulating the XML config file located at `/usr/lib/ugeeTablet/conf/Ugee_Tablet.xml`, after that, I simply run the driver and see the results. It took me a while to figure out how most things worked, unfortunately, some things still elude me.


I can't guarantee that the program will work on different version of the driver's configuration (e.g. Windows, Mac OS) as I focused on the GNU/Linux version only.


## How to use

Simply perform the cloning and execute the program:

```
git clone https://www.github.com/elluisian/ugeeconfig
cd ugeeconfig
./ugeeconfig.sh <commands>
```

See "Getting started" for some examples.


## Dependencies

In order for this program to work properly you need:

- Python 3.13.3, it should work with earlier versions too, I'm not sure though, I didn't use any fancy syntax, I don't believe at least;
- python3-xlib module;
- python3-lxml module;
- bash 5.2.37, older versions should also work, as long as the BASH_SOURCE variable array is supported;
- realpath and dirname utilities (used by the bash script);


## Getting started

While there's an help section, I admit it might not be enough for newcomers, since it is thought more of a "order of the parameters" reminder, more than an actual help, so, here it goes.

First, all the operators, commands, names, identifiers and such can be given in a CASE-INSENSITIVE manner, so, for example, you can refer to the UE16 tablet as "UE16", "ue16", "Ue16" and "uE16".
Don't worry about memorizing the precise case of letters.


### Getting to know the available props

To check for available properties (props), use the `doc` operator:

```
./ugeeconfig.sh doc <prop path>*
```

Here are two examples:

Get all devices plus deskkeys:

```
./ugeeconfig.sh doc
```

it returns:

```
RB160: Device data
BP1003W: Device data
[...]
UE16: Device data
deskkeys: Deskkeys data
```

Get the "UE16" and "deskkeys" props:

```
./ugeeconfig.sh doc UE16 deskkeys
```

it returns:

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

Props are defined as dotted paths (e.g. "UE16.pen.pressure", "deskkeys.zoom", etc), these ones are also CASE-INSENSITIVE, each one correlates to a single configurable setting for the tablets.

Please note that in order to avoid overwhelming the output with too much writings, the `doc` operator only shows the "direct children" of the input props.
In this example, by requesting "UE16", we're asking to show "UE16" and it's direct children, that is "UE16.pen", "UE16.tablet" and "UE16.settings", grand children (such as "UE16.pen.pressure") are ignored.

As can be seen, there are "node props" and "leaf props", the first ones are props that contain other props (e.g. "UE16", since it contains "pen", "tablet" and "settings"), the second ones on the other hand, are props with actual values that define the current configuration (e.g. "deskkeys.fixed" and "deskkeys.zoom"). It is very easy to distinguish them, as "leaf props" are the ones where their type is reported.
As a consequence of the above, only leaf props can be modified (set operator) and retrieved (get operator).



### Getting the props' values

To get the values of the available props, use the `get` operator:

```
./ugeeconfig.sh get <prop path>*
```

Some examples include:

Get all props' values:

```
./ugeeconfig.sh get
```

returns (the actual output is VERY long):

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
UE16.tablet.screenres: 1920x1080+0+0,sel=2
UE16.tablet.tabletres: 1342x755+0+0,rot=0
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

Get the props contained within "UE16.pen" and "deskkeys.vkey1":

```
./ugeeconfig.sh get UE16.pen deskkeys.vkey1
```

returns:

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

Please note that, if props are not correctly written, the program will try to detect possible valid props, basically, acting as a filter, the next example illustrates this behaviour:


```
./ugeeconfig.sh get UE16.pen.bu deskkeys.vkey1.action
```

returns:


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

This is also possible for the `doc` operator.



### Setting the props values

To set (leaf) props, use the `set` operator:

```
./ugeeconfig.sh set (prop, value pair)+
```

Contrary to early operators, the `set` operator an even number of operands in a "prop, value" pair fashion, in which first a prop to set is specified, then a value to assign to it. Here are some examples:

Enable pen pressure and set relative mode speed to 1 for the UE16 device:

```
./ugeeconfig.sh set UE16.pen.pressure.enabled t UE16.pen.relmode.speed 1
```

Value types that can be used and recognized are:

- Integers;
- Floats;
- Rectangles in the form "rect(x, y, w, h)", with "x", "y", "w", and "h" being integers;
- Pressure points in the form "press(p0, p1x, p1y, p2)", with "p0", "p1x", "p1y" and "p2" being integers;


Please note that the new resultant config file is shown as output, it is possible to redirect said output to a file and get a new XML config file, ready for use, but it is not the recommended way to make this.


#### How to set default actions (actids)

default_action's props can be set using an integer or the actual actid symbolic name.
The get a list of those, you can use the `actids` operator like this:

```
./ugeeconfig.sh actids (keys|mouse|funct|sysop|multim|all)*
```

The names on the right hand-side can be used to filter out certain kind of actids or "all" for everything.
Here's an example:

```
./ugeeconfig.sh actids funct
```

returns:

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


To edit a default action, for example, the UE16's pen button0's, you can do like this:


```
./ugeeconfig.sh set ue16.pen.button0.action_default funct_deskkeys
```

Please note that this is not possible on the official configuring program, but the driver itself supports it.




#### How to set custom actions


Custom actions are a bit tricky in comparison to earlier props and are the main reason I developed this program.
First of all, any actionable button has an `action_custom` node prop, each one of these has the following props:

- `label`: a simple label;
- `enabled`: a flag, if this is set, then the custom action is used;
- `action`: the actual custom action to use;

Please note that it is possible to properly store a custom action (`action` prop) without actually enabling it or without actually showing any label, in general, you want to set all three props at once, in order to have a complete custom action. The separation of these properties was done to add flexibility.


Custom actions may have one of the following forms:

- `keys(<keystroke>[,<keystroke>]*)` with`<keystroke>` having the form `<keysym>[\+<keysym>]*` (keysyms separated by pluses), basically, a list of keystrokes separated by commas;
- `mouse(<mouseactid>[\+<mouseactid>]*)` with `<mouseactid>` being a mouse actid (each mouse actid is separated by a plus);
- `exec(<execpath>)` with `<execpath>` being a path to an executable to be run. Please note that command line parameters are not supported, use custom scripts if needed;
- `funct(<functactid>)` with `<functactid>` being a function actid;
- `sysop(<sysopactid>)` with `<sysopactid>` being a sysop actid (not all of them work on GNU/Linux);
- `multim(<multimactid>)` with `<multimactid>` is a multimedia actid (none of them work on GNU/Linux, provided for completeness);
- `unset` or `unset()`, a special custom action that allows to completely wipe a previous defined custom action;
- `nop` or `nop()`, a special custom action that simply states that no action is performed, not even the default one;




#### How to set custom actions for wheel action movements

Wheel movements ("W" tags on the config file) are a totally different beast.
In fact, each single "wheel action movement" (that's how I decided to call them, I struggled to find a better name, bear with me), has two possible custom actions: a counterclockwise one and a clockwise one. Each action can only be of the "keys" type (keyboard input that is).

In general, each `"wheel_movement` prop, has the following props:

- `usage`: It determines what action is in use, it uses three keywords:
    - "usg\_default" for using the default action;
    - "usg\_nop" for not using actions, that is, no operation is performed;
    - "usg\_custom" for using the custom action;

- `label`: A label for the wheel action movement in general;
- `ccw_label`: The counterclockwise custom action's label;
- `cw_label`: The clockwise custom action's label;
- `ccw_action`: The counterclockwise (keys) custom action itself;
- `cw_action`: The clockwise (keys) custom action itself;


Here follows some examples:

```
./ugeeconfig.sh set ue16.tablet.r.wheel_movement4.usage usg_custom ue16.tablet.r.wheel_movement4.label "test" ue16.tablet.r.wheel_movement4.cw_action 'keys(ctrl)'
```


Please note that it is possible to set only one of the custom actions if needed.



#### X keysyms

The "keys type" of custom actions use what are called "X keysyms".
In X11's terminology these are symbols that properly define the keyboard inputs that X11 environments can handle.
There are many many X keysyms on GNU/Linux, this program only uses a few of them, provided by the Xlib module.

It is possible to use:

```
./ugeeconfig.sh xkeysyms
```

to show the available ones.
Please note that the output is very long, so it might be a good idea to save it to an external file via redirection, something like:

```
./ugeeconfig.sh xkeysyms > ugee_config-xkeysyms.txt
```

Another way to gather the correct xkeysyms is to use utilities like `xev`, which allows to detect xkeysyms associated with keyboard keys in real time, while pressing them.
Please note that different locales (utilities like ibus affect this the same way) will require different xkeysyms to perform the same action, in general, what is needed is not the output produced, but the keys used to reach that output.
Consider the left bracket character "[", to get that in Italian keyboards, you have to press AltGr followed by the grave accented E key. You may be tempted to configure a tablet key to use `keys(bracketleft)`, but in the Italian locale it won't work, what will is `keys(altgr+egrave)`.


### Reading and saving configuration files


Up to now, only a few props were shown, edited and documented, but all of this is useless if there is no way to actually make persistent config files.
Of course this is possible in a neat and clean way, by using the commands "from" and "to".
In short, "from" allows to load an already existing config file as a base for further modifications, "to" simply establishes where the resultant config file must be saved.

Basically, when "from" is omitted, a default config file is automatically generated by the program and used as a base for the modifications performed by the user. This is good in case you accidentally destroy something important and you want to start over, usually though, you want to further edit your own custom-made config files.

If "to" is omitted, the result is shown on stdout, as already established.


So, in order to load from a base file and save to another new file, just do the following:


```
./ugeeconfig.sh from <pathsrc> to <pathdest> set <operands>
```

The two paths may be the same, but I personally do not recommend this.

Here's a very simple example:

```
./ugeeconfig.sh from test.xml to test-edited.xml set ue16.pen.pressure.enabled true
```

Please note that `from` may be used with the `get` operator, to get current values within the specified base config file.