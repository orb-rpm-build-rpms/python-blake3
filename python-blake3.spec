Name:           python-blake3
Version:        1.0.9
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python bindings for the Rust blake3 crate

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        CC0-1.0 OR Apache-2.0
URL:            https://github.com/oconnor663/blake3-py
Source:         %{pypi_source blake3}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'blake3' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-blake3
Summary:        %{summary}

%description -n python3-blake3 %_description


%prep
%autosetup -p1 -n blake3-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files -l blake3


%check
%pyproject_check_import


%files -n python3-blake3 -f %{pyproject_files}


%changelog
%autochangelog
