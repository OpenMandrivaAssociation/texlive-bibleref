%global tl_name bibleref
%global tl_revision 75257

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.26.0
Release:	%{tl_revision}.1
Summary:	Format bible citations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bibleref
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bibleref package offers consistent formatting of references to parts
of the Christian bible, in a number of well-defined formats. It depends
on ifthen, fmtcount, and amsgen.

