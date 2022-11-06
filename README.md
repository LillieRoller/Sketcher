# Sketcher - Robot Artist

Sketcher is an [iRobot Root](https://edu.irobot.com/what-we-offer/root-robot) platform that draws line art drawn in [Google Drawings](https://en.wikipedia.org/wiki/Google_Drawings) and downloaded in [Scalable Vector Graphics](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) (SVG) format. 

# Development

Written in Python 3. 

1. Download and install [Visual Studio Code](https://code.visualstudio.com/)
2. Open a `terminal` or `command prompt`
3. `git clone https://github.com/LillieRoller/Sketcher.git` to download the project
4. `code Sketcher` to open the project in VSCode
5. Open in Dev Container (green bar in lower left corner)

## Dependencies 

Dependencies are encouraged to use other libraries that must be installed. 

Evaluate a dependency first by doing a manual install:

```
pip3 install pytest
```

When code is committed to the project that depends on it then add it to `requirements.txt` using the `==` operator to lock in a specific version.

> pytest==7.2.0

The dependency will be installed with:

```
pip3 install -r requirements.txt
```

NOTE: the installation line is run automatically when the devcontainer is created. 


# Test

## Run Tests in the Terminal

1. Open a terminal in the VSCode Dev Container
2. `pytest`

Expect a summary similar to ...


> ========== 1 passed in 0.08s ==========


## Run Tests in VS Code

1. Left sidebar -> Beaker Icon
2. Hover over `Sketcher`
3. Push `Run Test` play icon 

Results are displayed in Green passing and Red failures.
