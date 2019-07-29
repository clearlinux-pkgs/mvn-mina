#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-mina
Version  : 2.0.16
Release  : 1
URL      : https://github.com/apache/mina/archive/2.0.16.tar.gz
Source0  : https://github.com/apache/mina/archive/2.0.16.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/mina/mina-core/2.0.16/mina-core-2.0.16.jar
Source2  : https://repo1.maven.org/maven2/org/apache/mina/mina-core/2.0.16/mina-core-2.0.16.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-mina-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-mina package.
Group: Data

%description data
data components for the mvn-mina package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/mina/mina-core/2.0.16
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/mina/mina-core/2.0.16/mina-core-2.0.16.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/mina/mina-core/2.0.16
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/mina/mina-core/2.0.16/mina-core-2.0.16.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/mina/mina-core/2.0.16/mina-core-2.0.16.jar
/usr/share/java/.m2/repository/org/apache/mina/mina-core/2.0.16/mina-core-2.0.16.pom
