# Vectrabool

The aim of the project is to make a library for vectorization of a bitmap images, i.e., given an image in the bitmap format as input, transform it into vector image format SVG.
For more information, please refer to <a href='https://vladan-jovicic.github.io/Vec-Lib'>here</a>

## Dependencies

The following is required in order to compile the code:
- OpenCV (for Python 2.7 and C++)
- Numpy

## Installing Dependencies

- To install OpenCV, download <a href='https://drive.google.com/file/d/0B9EaSh0VvlsQOEN5bE5LU1U3b2s/view?usp=sharing'>script</a> and run the following commands:
```
chmod +x install_opencv.sh
./install_opencv.sh
```
<b>Remarks:</b>
- in the case that you get an error <i>Found unsuitable Qt version</i> run the following:
```
sudo apt-get install libqt4-dev pkg-config
```
and run the script again.

- To install python modules, run the following:
```
pip install -r requirements.txt
```

## Usage

You will find a few examples in folder <i>code_examples</i>

You can also use it as a gimp plugin:
- download files as a zip archieve
- extract gimp_plugin and vectrabool folders
- move vectrabool folder inside gimp_plugin
- open Gimp and go to <i>Edit/Preferences/Folders/Plugins</i>
- add path to the gimp_plugin folder

### Examples

This will be available soon


## TODO

- Improve color detection
- Remove OpenCV

## History

Update history

## Credits

The project is developed as a school project by a group of students from the ENS Lyon.

## License

This library is under the CeCILL v2 license

CeCILL FREE SOFTWARE LICENSE AGREEMENT
http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt



