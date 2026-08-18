Name:		python-multiprocess
Version:	0.70.19
Release:	1
Summary:	Better multiprocessing and multithreading in Python
License:		BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/uqfoundation/multiprocess
Source0:	https://files.pythonhosted.org/packages/source/m/multiprocess/multiprocess-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	python%{pyver}dist(dill)

%description
multiprocess is a fork of multiprocessing that uses dill for serialization,
so more Python types can be sent between processes. Required by Hugging Face
datasets.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/multiprocess
%{py_sitedir}/_multiprocess
%{py_sitedir}/multiprocess-*.*-info
