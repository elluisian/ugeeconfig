# UgeeConfig.xml documentation on the GNU/Linux platform

In this document I will describe my findings related to the XML file ugeeTabletDriver uses as its config file for setting pen buttons, tablet keys and so on.

Please note that I'm describing the linux version of the config file, as I work under there, to be precise, I work under Debian testing (Trixie, at the time of writing).
I didn't try the Windows version of the driver, so if things are implemented there but not here, I'm not aware, simply put.

Please also note that this is just a "trial-and-error documentation", no reverse engineering was performed, as my only goal was to set keystrokes easily, as keyboard events are totally diregarded in the official configuring program, making it hard to set those.


Let's start with the root node, which is named _UGEE_ and it includes the following nodes:

- __PenTabletLists__: It owns all the devices' definitions. It has a _version_ attribute, presumably used to detect the particular version of this node's "whole structure" (how the inner nodes are laid out that is);
- __DesktopShortcutKeys__: It owns all the information related to the "shortcut keys window", the one that may be used above everything else in-software (deskkeys in short from now on);


## DesktopShortcutKeys documentation

This node owns only a few inner nodes:

- __Fixed__: Will the deskkeys window be fixed or movable? 0 if fixed, 1 if not;
- __Zoom__: The "zoom" feature for the deskkeys (it causes the actions' icons to be bigger/smaller). Apparently the only supported values are "1", "1.5" and "2";
- __DisplayedAtCursor__: I have no idea what this does, perhaps used in some other tablets? If not used at all, it probably would have been used so that the deskkeys window could be shown near the cursor (like a popup menu);
- __Rows__: Number of rows available in the deskkeys window. According to the configuring program, the maximum should be 4;
- __Columns__: Number of columns available in the deskkeys window. According to the configuring program, the maximum should be 4;


## Single device documentation

Each device definition starts with a tag representing its code name, throughout this document, I will refer to the UE16 tablet as an example, as it happens this is the device I personally own.

Basically, for the UE16, the node's tag is "UE16", for other models, it's their code name.

Every device node contains the following nodes:

- __DeviceInfo__) Its inner nodes describe the features of the particular device:
    - __DeviceRingNum__) As the name suggests, it is the number of available rings (can be thought as "knobs") on the tablet. The UE16 for example features one of them, it is possible to assign two different actions to it, based on the particular rotation's direction, be it clockwise or counterclockwise;
    - __DeviceKeyNum__) As the name suggests, it is the number of available physical keys on the tablet;
    - __DevicePenType__) It is an integer value that supposedly describes the features of the pen used by the tablet. Unfortunately, I can't investigate further as I own only the UE16;
    - __DeviceTrackpad__) Not sure what this does, perhaps it establishes if the tablet can be treated as a trackpad;
    - __DeviceControl__) Not sure what this does;
    - __DeviceKeyDirection__) Only a few devices have this, I'm not sure what's supposed to mean;

- __Common__) Common properties, not related to "apps" (see below):
    - __ScreenMapping__) It establishes what is the "walkable" area of the screen on the tablet when using the pen. This is used for those tablets that also feature a monitor, such as the UE16. Basically, with this option, it is possible to enlarge or restrict the reachable areas of the screen when using the pen to navigate:
        - The _id_ attribute is used to record the dropdown menu choice, when selecting the monitor (0 is the first entry);
        - Nodes __SX__, __SY__, __SW__ and __SH__ simply define, in pixel, the mapping (coordinate 0,0 is on the top-left);


    - __TabletPannel__) It establishes what is the usable area on the tablet that may be used to "walk the screen". This is used for those tablets that also feature a monitor, such as the UE16. Basically, with this option, it is possible to determine the precise portion of the tablet screen that must be touched by the pen, in order to perform some kind of movement on the screen:
        - The _Orientation_ attribute is used to determine the tablet's orientation. 0 is standard, 1 is 90°, 2 is 180° and 3 is 270°;
        - Nodes __TX__, __TY__, __TW__ and __TH__ simply define, in pixel, the mapping (coordinate 0,0 is on the top-left);
    - __DisableInfo__) Show "messages" when using keys/rotating buttons, and so on (0 to enable, 1 to disable);
    - __DisableQuickKey__) Contrary to its counterintuitive name, this is used to determine if tablet keys should produce any input or not (0 to enable tablet keys input, 1 to disable);
    - __DisablePressure__) Detect pen pressure (0 to enable, 1 to disable);
    - __DisableSlope__) Detect pen tilt (0 to enable, 1 to disable);
    - __PictureFiles__) I don't know where this is used. I speculate these represent the particular device's images used in the configuring program, I'm not sure though:
        - __T_0__) A rectangle described by the attributes _X_, _Y_, _W_ and _H_, all integers;
        - __T_1__) Same as __T_0__;
        - __T_2__) Same as __T_0__;
        - __T_3__) Same as __T_0__;


    - __SC__) I don't know what this is supposed to be, not all devices have this:
        - attributes _fXY_, _fXLC_, _fYLC_ and _fKX_: if __SC__ is present, all of these are set to 1. I don't know what these are;


- __CommonAPP__) Common properties that apply regardless of the particular "app" (see below):
    - __Pen__) Properties of the pen:
        - __PenBtn\<N\>__) Particular pen button, its "tag number" _\<N\>_ is important, as not all the devices have the same set of tag numbers. Some might even not present any button, in that case, this node is absent.
            - The _id_ attribute is used to determine if a custom action is set, 1 if set, 0 if not;
            - The _Actid_ attribute is used to determine the default action of the button, when no custom action is set (also used during the config reset in the configuring program);
            - If a custom action is set, the content is set to the action definition (see Action documentation for details);
        - __P0__, __P1X__, __P1Y__ and __P2__) Respectively, starting point, middle point and ending point, these are used to represent the pressure curve. __P0__ and __P2__ represent the starting and ending X axis (with P0's Y being 0 and P2's Y being 1), the middle point on the other hand, have both X and Y axes;
        - __TablePC__) Not sure what this means, I've seen it's always set to 1;
        - __RelativeCoords__) These are the settings related to "mouse mode":
            - The _Speed_ attribute is an integer from 0 to 10, with 5 as its default;
            - The content is set to 0 if disabled, 1 if enabled;


    - __K__) Description of tablet keys's actions:
        - __K\<N\>__) Particular tablet key, its "tag number" _\<N\>_ is important, as not all the devices have the same set of tag numbers. Some might even not present any key, in that case, this node is absent:
            - The _id_ attribute is used to determine if a custom action is set, 1 if set, 0 if not;
            - The _Actid_ attribute is used to determine the default action of the key, when no custom action is set (also used during the config reset in the configuring program);
            - The _Motid_ attribute is usually set exactly to the tag number of the particular key, this doesn't apply to the "Q6" device for some reason, as the different "motids" are set backwards in respect to the tag number. I honestly don't know what is supposed to mean;
            - The _Show_ attribute may have been used to hide entries, it doesn't appear to work though. If I decide to set Show to 0 on one of the keys, the configuring program doesn't run. Perhaps this was used during debugging? For some odd reason, UE16 has the 9th key, located at the center of the ring, set with Show=0, if it is changed to Show=1, the configuring program does not show up, but the driver works properly.
            - If a custom action is set, the content is set to the action definition (see Action documentation for details);


    - __R__) Description of the first ring of the tablet. If the tablet has no rings, this node is absent. A ring may have multiple "wheel actions" (represented by the __W__ node, see below):
        - the _id_ attribute is used to determine what particular "wheel action" is used (0 is the first one);
        - __W\<N\>__) A single "wheel action", which is basically a pair of actions, one for clockwise movement, the other for counterclockwise movement. Most tablets have up to 4 wheel actions, for some reason though, the LPU1102 has five of them:
            - The _id_ attribute is used to determine the kind of action that is set. If 0, then the default action is set, if 1 then the wheel action has no effect, if 2, then a custom wheel action is set;
            - If a custom wheel action is set, the content is set to the wheel action definition (see Action documentation for details, in particular "Action Type 4: wheel actions");
            - Please note that, contrary to the tags owning the _actid_ attribute, it seems there is no way to change the default wheel action;


    - __R2__) Description of the second ring of the tablet. If the tablet has no rings or no second ring, this node is absent;
        - the _id_ attribute is the same as __R__'s;
        - the _mode_ attribute is used to determine the "mode"... too bad I don't know what that means;
        - __W\<N\>__) Same as __R__'s;


    - __TR__) Alternative description of the second ring of the tablet. For some reason, this is used, instead of "R2", only on the LPU1505F device. Apart from that, it's equivalent to __R2__;



- __Apps__) Properties that apply to particular "apps". As reported in "22.3.5 Applications and Others" of the page [https://www.ugee.com/subsidiary/setup-ue16](https://www.ugee.com/subsidiary/setup-ue16), it is possible to add per-app settings, unfortunately, it seems only the windows version of the drivers allows for this.
    - __app__) A single app. For some reason, the configuring program makes only a single app entry, with _id_ set to 0 and _name_ set to 0... Is this some sort of default entry? Nonetheless, these "apps" are ignored on GNU/Linux, :
        - The _id_ attribute is used for... well... I don't know;
        - The _name_ attribute is used, I guess, to define a friendly name for the app;
        - __path__) A supposed path to an executable, I guess;
        - The rest of tags mimic the ones contained in __CommonAPP__, except that, for some reason, the __K__ nodes of the "id=0" app entry have no attributes besides _id_;



## Action documentation

Now, the reason I decided to develop ugeeconfig in the first place.

The main problem I had was the configuring program completely ignoring input from keyboard, making it difficult to set custom actions as keystrokes for the tablet/pen. Other than that, even if enabled, "messages" would not show up, AT ALL. Other problems include the complete non-working of deskkeys and all the commands related to show/hide the configuring program and/or deskkeys window.
I tinkered with the QT5 framework, but I was not capable of finding any way to solve and/or reproduce the problem reliably, because of that, I decided to make some kind of command-line editor, just to simplify things when defining custom actions, in the hope that in the future the remainder of bugs get solved.

To set actions, there are two main ways:

- Default actions, identified by the _Actid_ attribute. These can be set to __K__ nodes (tablet keys and deskkeys) and __PenBtn__ nodes;

- Custom actions, defined in the contents of the particular key/virtual key/button/wheel movement's node;



### Default actions: the Actid attribute

In the context of the configuring program, actids are used to assign action to keys/buttons when no custom action is set. They are also used for resetting the configuration when choosing "restore configuration".
Theoretically, each keys/buttons/etc has its own particular default actionid that is immutable, in practice though, it is possible to force a particular actionid by writing it in the XML config file itself.

Here follows the list of actionids that were found out during the development of ugeeconfig, these should be all, though I'm not sure:


Actid |            Description/Effect |                                            Notes
:----:|:-----------------------------:|:-----------------------------------------------:
|     |   DRIVER FUNCTS. DESCRIPTIONS | All unusable except for "10" (No function set)
    1 |                    Pen/Eraser |
    2 |                     Mouse key |
    3 |                     Keystroke |
    4 |                        Device |
    5 |               Run application |
    6 |               System function |
    7 |                    Multimedia |
   10 |                   No function |                                No function set
   11 |                     Customize |
   12 |                       Default |
|&nbsp;|                              |
|     |        MOUSE KEY COMBINATIONS |
  201 |                         Shift |
  202 |                      Left Alt |
  203 |                     Right Alt |
  204 |                          Ctrl |
  205 |                         Space |
  206 |                    Left Click |
  207 |                   Right Click |
  208 |                  Scroll Click |
  209 |             Left double click |
  210 |                     Scroll up |
  211 |                   Scroll down |
|&nbsp;|                              |
|     |        PREDEFINED KEY STROKES |
  301 |                 Keystroke "B" |
  302 |                 Keystroke "E" |
  303 |               Keystroke "Alt" |
  304 |             Keystroke "Space" |
  305 |            Keystroke "Ctrl+S" |
  306 |            Keystroke "Ctrl+Z" |
  307 |        Keystroke "Ctrl+Alt+Z" |
  308 |      Keystroke "Ctrl+Shift+Z" |
  309 |                 Keystroke "V" |
  310 |                 Keystroke "L" |
  311 |            Keystroke "Ctrl+O" |
  312 |            Keystroke "Ctrl+N" |
  313 |      Keystroke "Ctrl+Shift+N" |
  314 |            Keystroke "Ctrl+E" |
  315 |                 Keystroke "F" |
  316 |                 Keystroke "D" |
  317 |                 Keystroke "X" |
  318 |       Keystroke "Ctrl+Delete" |
  319 |            Keystroke "Ctrl+C" |
  320 |            Keystroke "Ctrl+V" |
  321 |            Keystroke "Ctrl++" |
  322 |            Keystroke "Ctrl+-" |
  323 |               Keystroke "Tab" |
  324 |                Keystroke "F5" |
  325 |                 Keystroke "]" |
  326 |                 Keystroke "[" |
  327 |            Keystroke "Ctrl+]" |
  328 |            Keystroke "Ctrl+[" |
|&nbsp;|                              |
|     |                     FUNCTIONS |
  401 | Display/Hide Driver Interface |
  402 |                Switch monitor |
  403 |                    Pen/Eraser |
  404 |                Precision mode |
  405 |         Switch ring1 function |
  406 |         Switch ring2 function |       Available only on devices with two rings
  407 |          Change trackpad mode |    Not sure what "trackpad" is in this context
  408 |                       [B]/[E] |
  409 |                        Eraser |
  410 |                     Desk keys |
|&nbsp;|                              |
|     |             SYSTEM OPERATIONS |
  601 |                   Lock screen |                       Not working on GNU/Linux
  602 |                      Shutdown |
  603 |                     Hibernate |
  604 |               Show activities |                       Not working on GNU/Linux
  605 |                  Startup menu |                       Not working on GNU/Linux
|&nbsp;|                              |
|     |         MULTIMEDIA OPERATIONS |                None of these work on GNU/Linux
  701 |                      Previous |
  702 |                          Next |
  703 |                    Play/Pause |
  704 |                       Volume+ |
  705 |                       Volume- |
  706 |                          Mute |


The configuring program makes a default config file with unique actid combinations per button/key etc for every single supported device. For more details check the "DefaultConfigs.py" file, which is responsible for the re-generation of the default XML config file.


### Custom actions: Action type \<N\>

There are 8 types of custom actions, depending on the desired behaviour that one wants to assign to buttons/virtual keys/keys/wheel movements.
The following paragraphs will describe each custom action type in detail.



### Action Type 1: Keystroke

When the particular key is pressed, one or more keystroke events are generated.

Please note that this paragraph's info is valid only for the GNU/Linux version of the driver, as it relies on X11 keysyms/keycodes.

Its format is:

```
1||<label>|<keystrokes>
```

where:

- `<label>` is a string representing the keystrokes. The configuring program simply sets this to the name of all the entered keystrokes;

- `<keystrokes>` is a list of comma-separated `<keystroke>` elements;

- A `<keystroke>` is made of one or multiple plus-separated `<key>` elements. A single `<key>` has the format `<keysym>:<keycode>` where `<keysym>` is the X keysym (in decimal) of the `<key>` and `<keycode>` is the keycode (in decimal) of the `<key>`. Both of them can be obtained by using the `xev` utility (remember to convert the keysym to decimal, in `xev` that is given in hexadecimal);


Here's an example:

```
1||Ctrl+Alt+A,Alt+B|65507:37+65513:64+97:38,65513:64+98:56
```

Let's see why we get `65507:37+65513:64+97:38` for Ctrl+Alt+A and `65513:64+98:56` for Alt+B.\
Run `xev` and gather the keys Ctrl, Alt, A and B. Here follows the output from my own system:

```
[...]

KeyPress event, serial 38, synthetic NO, window 0x6000001,
    root 0x3e2, subw 0x6000002, time 37149253, (41,45), root:(1781,497),
    state 0x10, keycode 37 (keysym 0xffe3, Control_L), same_screen YES,
    XLookupString gives 0 bytes: 
    XmbLookupString gives 0 bytes: 
    XFilterEvent returns: False

<[...]

KeyPress event, serial 38, synthetic NO, window 0x6000001,
    root 0x3e2, subw 0x6000002, time 37094557, (31,34), root:(1771,486),
    state 0x10, keycode 64 (keysym 0xffe9, Alt_L), same_screen YES,
    XLookupString gives 0 bytes: 
    XmbLookupString gives 0 bytes: 
    XFilterEvent returns: False

[...]

KeyPress event, serial 38, synthetic NO, window 0x6000001,
    root 0x3e2, subw 0x6000002, time 37147894, (41,45), root:(1781,497),
    state 0x10, keycode 38 (keysym 0x61, a), same_screen YES,
    XLookupString gives 1 bytes: (61) "a"
    XmbLookupString gives 1 bytes: (61) "a"
    XFilterEvent returns: False

[...]

KeyPress event, serial 38, synthetic NO, window 0x6000001,
    root 0x3e2, subw 0x6000002, time 37042662, (28,45), root:(1768,497),
    state 0x10, keycode 56 (keysym 0x62, b), same_screen YES,
    XLookupString gives 1 bytes: (62) "b"
    XmbLookupString gives 1 bytes: (62) "b"
    XFilterEvent returns: False

[...]
```

From this output, it can be concluded that:

- For Ctrl, the keysym is 0xffe3 (65507 in decimal) and the keycode is 37. Ergo, to represent it, one has to write "65507:37";

- For Alt, the keysym is 0xffe9 (65513 in decimal) and the keycode is 64. Ergo, to represent it, one has to write "65513:64";

- For A, the keysym is 0x61 (97 in decimal) and the keycode is 38. Ergo, to represent it, one has to write "97:38";

- For B, the keysym is 0x62 (98 in decimal) and the keycode is 56. Ergo, to represent it, one has to write "98:56";



### Action Type 2: Mouse key

When the key is pressed, one or more mouse plus some arbitrary control keys events are generated. Its format is:

```
2||<label>|<keys>+<click>
```

where:

- `<label>` is a string representing the mouse clicks and control keys. The configuring program simply sets this to the name of all the entered keys/clicks;


- `<keys>` is a set of one or more actids (range 201-205), separated by a plus;
- `<click>` is an actid among 206 to 211;


Here are two examples:

```
2||Ctrl+Left click|204+206
2||Left double click|209
```



### Action Type 3: Driver functions


This action type is strictly related to the interaction with the ugee configuring program and/or the deskkeys window. Its format is:

```
3||<label>|<function>
```

where:

- `<label>` is a string representing the particular chosen function;
- `<function>` is an actid among 401 to 410;


Some examples are presented below:

```
3||Pen/Eraser|403
3||Eraser|409
3||Desktop shortcut keys|410
```



### Action Type 5: Executing programs

As the name suggests, with this action type, it is possible to press some keys in order to run executables. Its format is:

```
5||<label>|<path>
```


where:

- `<label>` is a label for the executable. The configuring program sets this to the basename of the executable;
- `<path>` is an absolute path to an executable. Command line arguments are not supported;


Here follows an example:

```
5||glxgears|/usr/bin/glxgears
```



### Action Type 6: System operations

This action type is related to the execution of system operations, its format is:


```
6||<label>|<sysop>
```

where:

- `<label>` is a label for the particular operation;
- `<sysop>` is an actid among 601 to 605;


Here below are two examples:

```
6||Shutdown|602
6||Hibernate|603
```



### Action Type 7: Multimedia functions

This action type's commands simply executes some multimedia actions (play/pause etc..).\
Even when forced, this action type does not work on GNU/Linux.\
Its format is the following:


```
7||<label>|<multimediaop>
```


where:

- `<label>` is a label for the particular multimedia operation;
- `<multimediaop>` is an actid among 701 to 706;


An example of this is:

```
7||Previous|701
```



### Action Type 10: Unused

This is used when selecting "no function", that is, the button/key is not mapped to anything, not even it's default action. Its format is:


```
10|No function|No function
```

In reality, the two texts are simple labels, they change according to the language, so it shouldn't matter what is actually written there, what is actually important, is the "10" value.



### Action type 4: Wheel actions

Some tablets, like the UE16, have one or more "rings" (they are called "rollers" in the FAQs). These are rotable knobs that if rotated in a certain direction, a certain action is performed.

For each ring, there are up to 4 possible wheel actions (that's how I decided to call them, poor name, I know), that is, a pair of single actions, one for clockwise movement and the other for counterclockwise movement.\
A ring can use only one wheel action at a time, but it is possible to cycle over them (with actids 405 and 406).

This action type applies to the __W\<N\>__ element, when it is set, its _id_ attribute is set to 2 and its contents have the following format:

```
4|<label>|<ccwlabel>|<cwlabel>|<ccwkstrokes>|<cwkstrokes>
```

where:

- `<label>` is supposed to be a label describing the pair of actions. As far as I noticed, the configuring program sets this to "custom";
- `<ccwlabel>` is the label for the counterclockwise action. The configuring program sets it based on the entered keys;
- `<cwlabel>` is the label for the clockwise action. The configuring program sets it based on the entered keys;
- `<ccwstrokes>` is a `<keystrokes>` element, as defined in the section "Action Type 1: Keystrokes". This one is used when performing the counterclockwise movement;
- `<cwstrokes>` is a `<keystrokes>` element, as defined in the section "Action Type 1: Keystrokes". This one is used when performing the clockwise movement;


As already said, contrary to other type of keys/buttons, the pair of custom actions can only be keystrokes, the same ones already treated in the section "Action Type 1: Keystrokes".

In the following example:

```
4|Customize|A|B|97:38|98:56
```

If a clockwise rotation is performed then the letter "A" will be produced, if a counterclockwise rotation is performed, "B" is produced.

Please note that it is also possible to define only one of the two available custom action, consider the following:

```
4|Customize|A||97:38|
```

In this case, only the clockwise rotation produces something ("A").