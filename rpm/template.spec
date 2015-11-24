Name:           ros-indigo-ecl-mobile-robot
Version:        0.60.1
Release:        0%{?dist}
Summary:        ROS ecl_mobile_robot package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ecl_mobile_robot
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-ecl-build
Requires:       ros-indigo-ecl-errors
Requires:       ros-indigo-ecl-formatters
Requires:       ros-indigo-ecl-geometry
Requires:       ros-indigo-ecl-license
Requires:       ros-indigo-ecl-linear-algebra
Requires:       ros-indigo-ecl-math
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-ecl-build
BuildRequires:  ros-indigo-ecl-errors
BuildRequires:  ros-indigo-ecl-formatters
BuildRequires:  ros-indigo-ecl-geometry
BuildRequires:  ros-indigo-ecl-license
BuildRequires:  ros-indigo-ecl-linear-algebra
BuildRequires:  ros-indigo-ecl-math

%description
Contains transforms (e.g. differential drive inverse kinematics) for the various
types of mobile robot platforms.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Nov 24 2015 Daniel Stonier <d.stonier@gmail.com> - 0.60.1-0
- Autogenerated by Bloom

