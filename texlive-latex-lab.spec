%global tl_name latex-lab
%global tl_revision 79404

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2026~06~01a
Release:	%{tl_revision}.1
Summary:	LaTeX laboratory
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/required/latex-lab
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-lab.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-lab.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-lab.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle holds optional files that are loaded in certain situations
by kernel code (if available). While this code is still in development
and the use is experimental, it is stored outside the format so that
there can be intermediate releases not affecting the production use of
LaTeX. Once the code is finalized and properly tested it will eventually
move to the kernel and the corresponding file in this bundle will
vanish. Note that none of these files are directly user accessible in
documents (i.e., they aren't packages), so the process is transparent to
documents already using the new functionality.

