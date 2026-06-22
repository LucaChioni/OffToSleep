# Running and Building the Game

> **Important**
>
> If you download the project from GitHub, the game will not work as-is because all audio and video resources are missing.

## Requirements

### Windows and Linux

The game must be run with **Python 2** and the following library versions:

```txt
pygame==1.9.6
cx-freeze==5.0.1
psutil==5.8.0
```

### macOS

The game must be run with **Python 3** and the following library versions:

```txt
pygame==2.1.2
cx-freeze==6.13.1
psutil==5.8.0
```

## Running the Game

Before running the code, update the following settings:

1. Open:

```txt
FileProgetto/GlobalHWVar.py
```

2. On line 12, set the operating system. Choose one of the following values:

```python
"Windows"
"Linux"
"Mac"
```

3. On line 14, set the `usando_python3` variable:

```python
usando_python3 = False
```

Use `False` if you are running the game on **Windows** or **Linux**.

```python
usando_python3 = True
```

Use `True` if you are running the game on **macOS**.

## Creating the Executable

Before creating the executable, update the following settings:

1. Open:

```txt
FileProgetto/setup.py
```

2. On line 4, set the operating system. Choose one of the following values:

```python
"Windows"
"Linux"
"Mac"
```

3. Open:

```txt
FileProgetto/GlobalHWVar.py
```

4. On line 13, set the `eseguibile` variable to `True`:

```python
eseguibile = True
```

5. Run the script for your operating system:

### Windows

```txt
Convertire_in_eseguibile_windows.bat
```

### Linux

```bash
./Convertire_in_eseguibile_linux.sh
```

### macOS

```bash
./Convertire_in_eseguibile_mac.sh
```

6. The executable will be created inside the `build` folder.
