
# | Escape Sequence | Meaning                                   | Example                | Output                              |
# | --------------- | ----------------------------------------- | ---------------------- | ----------------------------------- |
# | `\'`            | Single quote                              | `'It\'s fine'`         | It's fine                           |
# | `\"`            | Double quote                              | `"He said \"Hello\""`  | He said "Hello"                     |
# | `\\`            | Backslash                                 | `'C:\\path\\file.txt'` | C:\path\file.txt                    |
# | `\n`            | New line                                  | `'Hello\nWorld'`       | Hello<br>World                      |
# | `\t`            | Horizontal tab                            | `'Name:\tVinod'`       | Name: Vinod                         |
# | `\r`            | Carriage return                           | `'Hello\rWorld'`       | World                               |
# | `\b`            | Backspace                                 | `'Helloo\b'`           | Hello                               |
# | `\f`            | Form feed                                 | `'Hello\fWorld'`       | (New page break, depends on system) |
# | `\v`            | Vertical tab                              | `'Hello\vWorld'`       | Hello<br> World                     |
# | `\ooo`          | Octal value                               | `'\101'`               | A                                   |
# | `\xhh`          | Hexadecimal value                         | `'\x41'`               | A                                   |
# | `\N{name}`      | Unicode character by name                 | `'\N{copyright sign}'` | ©                                   |
# | `\uXXXX`        | 16-bit Unicode (Basic Multilingual Plane) | `'\u03A9'`             | Ω                                   |
# | `\UXXXXXXXX`    | 32-bit Unicode (Extended Plane)           | `'\U0001F600'`         | 😀                                  |


# Single quote
print("It\'s me")

#Double quote He said "Hello"

print("He said \"Hello\"")

#  Backslash C:\path\file.txt
print("C:\\path\\file.txt")

#New line  Hello
#            World

print("Hello \n    world")
#print("Hello",end='\n',"world") -- > not valid bcz end works for whole line

# Carriage return World
print("Hello \r world")

#Form feed
print("Hello \fworld")

#Vertical tab
print("mynameis\vAUT")