![](http://i59.tinypic.com/23qxaj9.png)

**pyQSS** is a tool that allows embedding **Python code in Qt Style Sheets** (QSS) files in order to make them easier to maintain, keep consistent and dynamic.

QSS file is enhanced with Python snippets in the form of:
@<...>@ and $<...>$ , where
* @ -- python code will be executed with exec() function (good for defining variables)
* $ -- python code will be executed with eval() function (good for including results of computations)

Additionally, a small set of utility classes and methods is provided in helpers.py. These should make integration with QSS more seamless and should be easy to extend.

A simple example is given: see file example.pyqss

To run the pyQSS on the example use the following command: "python pyQSS.py example.pyqss example_result.qss"


***
  _Copyright Artem Amirkhanov 2014_
  _Distributed under the MIT Software License (See accompanying file LICENSE.txt)_

  _Contact the author: artem.ogre@gmail.com_

