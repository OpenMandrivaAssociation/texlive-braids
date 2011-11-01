Name:		texlive-braids
Version:	1.0
Release:	1
Summary:	Draw braid diagrams with PGF/TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/braids
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/braids.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/braids.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/braids.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package enables drawing of braid diagrams with PGF/TikZ
using a simple syntax. The braid itself is specified by giving
a word in the braid group, and there are many options for
styling the strands and for drawing "floors".

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/braids/braids.sty
%doc %{_texmfdistdir}/doc/latex/braids/README
%doc %{_texmfdistdir}/doc/latex/braids/braids_doc.pdf
%doc %{_texmfdistdir}/doc/latex/braids/braids_doc.tex
#- source
%doc %{_texmfdistdir}/source/latex/braids/braids.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
