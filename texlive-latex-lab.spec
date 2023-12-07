Name:		texlive-latex-lab
Version:	68720
Release:	1
Summary:	LaTeX laboratory
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/latex-lab
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-lab.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-lab.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-lab.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The LaTeX laboratory provides a route for additions to the
LaTeX kernel to be stablised, whilst still allowing some
stability for adventorous users.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/latex-lab
%{_texmfdistdir}/tex/latex/latex-lab
%doc %{_texmfdistdir}/doc/latex/latex-lab

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
