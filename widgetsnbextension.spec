#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : widgetsnbextension
Version  : 3.1.0
Release  : 18
URL      : https://pypi.python.org/packages/49/15/e30906c394e83bd969807e27ffbe487b678c59939b3131184cb50d115473/widgetsnbextension-3.1.0.tar.gz
Source0  : https://pypi.python.org/packages/49/15/e30906c394e83bd969807e27ffbe487b678c59939b3131184cb50d115473/widgetsnbextension-3.1.0.tar.gz
Summary  : IPython HTML widgets for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause
Requires: widgetsnbextension-python3
Requires: widgetsnbextension-data
Requires: widgetsnbextension-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package data
Summary: data components for the widgetsnbextension package.
Group: Data

%description data
data components for the widgetsnbextension package.


%package python
Summary: python components for the widgetsnbextension package.
Group: Default
Requires: widgetsnbextension-python3

%description python
python components for the widgetsnbextension package.


%package python3
Summary: python3 components for the widgetsnbextension package.
Group: Default
Requires: python3-core

%description python3
python3 components for the widgetsnbextension package.


%prep
%setup -q -n widgetsnbextension-3.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1514391791
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/nbextensions/jupyter-js-widgets/extension.js
/usr/share/jupyter/nbextensions/jupyter-js-widgets/extension.js.map

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
