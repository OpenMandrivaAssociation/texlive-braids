%global tl_name braids
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3
Release:	%{tl_revision}.1
Summary:	Draw braid diagrams with PGF/TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/braids
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/braids.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/braids.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/braids.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables drawing of braid diagrams with PGF/TikZ using a
simple syntax. The braid itself is specified by giving a word in the
braid group, and there are many options for styling the strands and for
drawing "floors".

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/braids
%dir %{_datadir}/texmf-dist/source/latex/braids
%dir %{_datadir}/texmf-dist/tex/latex/braids
%doc %{_datadir}/texmf-dist/doc/latex/braids/README.txt
%doc %{_datadir}/texmf-dist/doc/latex/braids/braids.pdf
%doc %{_datadir}/texmf-dist/doc/latex/braids/braids.tex
%doc %{_datadir}/texmf-dist/doc/latex/braids/braids_code.pdf
%doc %{_datadir}/texmf-dist/source/latex/braids/braids_code.dtx
%doc %{_datadir}/texmf-dist/source/latex/braids/braids_code.ins
%{_datadir}/texmf-dist/tex/latex/braids/braids.sty
%{_datadir}/texmf-dist/tex/latex/braids/tikzlibrarybraids.code.tex
