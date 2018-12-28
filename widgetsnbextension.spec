#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : widgetsnbextension
Version  : 3.4.2
Release  : 39
URL      : https://files.pythonhosted.org/packages/cb/37/ec01aac3e510645959795337bf652155cd7efb28aecc940b0773e8ba8e4d/widgetsnbextension-3.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/cb/37/ec01aac3e510645959795337bf652155cd7efb28aecc940b0773e8ba8e4d/widgetsnbextension-3.4.2.tar.gz
Summary  : IPython HTML widgets for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause
Requires: widgetsnbextension-python3
Requires: widgetsnbextension-license
Requires: widgetsnbextension-data
Requires: widgetsnbextension-python
Requires: notebook
BuildRequires : buildreq-distutils3
Patch1: change-widgetsnbextension-json-path.patch

%description
No detailed description available

%package data
Summary: data components for the widgetsnbextension package.
Group: Data

%description data
data components for the widgetsnbextension package.


%package license
Summary: license components for the widgetsnbextension package.
Group: Default

%description license
license components for the widgetsnbextension package.


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
%setup -q -n widgetsnbextension-3.4.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536976477
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/widgetsnbextension
cp LICENSE %{buildroot}/usr/share/doc/widgetsnbextension/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/nbextensions/jupyter-js-widgets/extension.js
/usr/share/jupyter/nbextensions/jupyter-js-widgets/extension.js.map
/usr/share/jupyter/nbextensions/nbconfig/notebook.d/widgetsnbextension.json

%files license
%defattr(-,root,root,-)
/usr/share/doc/widgetsnbextension/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
