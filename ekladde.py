# -*- coding: iso-8859-1 -*-

"""
    MoinMoin - eKladde theme

    Based on MemoDump theme which in turn is
    Based on modernized theme in MoinMoin

    Config variables:
        Following variables and methods in wikiconfig.py will change something in the theme.

            Overrides menu elements.

        memodump_menu_def(request)
            Additional data dictionary of menu items.

        memodump_hidelocation
            Overrides list of page names that should have no location area.
            e.g. [page_front_page, u'SideBar', ]

    References:
        How to edit menu items:
            https://github.com/dossist/moinmoin-memodump/wiki/EditMenu
        Tips:
            https://github.com/dossist/moinmoin-memodump/wiki/Tips

    @copyright: 2014 dossist.
    @copyright: 2021 gejosch
    @license: GNU GPL, see http://www.gnu.org/licenses/gpl for details.
"""

from MoinMoin.theme import ThemeBase
import StringIO, re
from MoinMoin import wikiutil
from MoinMoin.action import get_available_actions
from MoinMoin.Page import Page
from MoinMoin.macro.NewPage import NewPage

class Theme(ThemeBase):

    name = "ekladde"

    _ = lambda x: x     # We don't have gettext at this moment, so we fake it
    icons = {
        # key         alt                        icon filename      w   h
        # FileAttach
        'attach':     ("%(attach_count)s",       "bi/paperclip.svg",   16, 16),
        'info':       ("[INFO]",                 "bi/info-square-fill-blue-white.svg",     16, 16),
        'attachimg':  (_("[ATTACH]"),            "bi/paperclip.svg",        32, 32),
        # RecentChanges
        'rss':        (_("[RSS]"),               "bi/rss.svg",      16, 16),
        'deleted':    (_("[DELETED]"),           "bi/file-earmark-x-black-red.svg",  16, 16),
        'updated':    (_("[UPDATED]"),           "moin-updated.png",  16, 16),
        'renamed':    (_("[RENAMED]"),           "moin-renamed.png",  16, 16),
        'conflict':   (_("[CONFLICT]"),          "bi/x-square.svg", 16, 16),
        'new':        (_("[NEW]"),               "bi/file-plus-green.svg",      16, 16),
        'diffrc':     (_("[DIFF]"),              "bi/files.svg",     16, 16),
        # General
        'bottom':     (_("[BOTTOM]"),            "moin-bottom.png",   16, 16),
        'top':        (_("[TOP]"),               "moin-top.png",      16, 16),
        'www':        ("[WWW]",                  "moin-www.png",      16, 16),
        'mailto':     ("[MAILTO]",               "moin-email.png",    16, 16),
        'news':       ("[NEWS]",                 "moin-news.png",     16, 16),
        'telnet':     ("[TELNET]",               "moin-telnet.png",   16, 16),
        'ftp':        ("[FTP]",                  "moin-ftp.png",      16, 16),
        'file':       ("[FILE]",                 "moin-ftp.png",      16, 16),
        # search forms
        'searchbutton': ("[?]",                  "moin-search.png",   16, 16),
        'interwiki':  ("[%(wikitag)s]",          "moin-inter.png",    16, 16),

        # smileys (this is CONTENT, but good looking smileys depend on looking
        # adapted to the theme background color and theme style in general)
        #vvv    ==      vvv  this must be the same for GUI editor converter
        'X-(':        ("X-(",                    'bi/emoji-angry-fill-yellow.svg',         16, 16),
        ':D':         (":D",                     'bi/emoji-laughing-fill-yellow.svg',       16, 16),
        '<:(':        ("<:(",                    'bi/emoji-frown-fill-yellow.svg',         16, 16),
        ':o':         (":o",                     'redface.png',       16, 16),
        ':(':         (":(",                     'bi/emoji-frown-fill-yellow.svg',           16, 16),
        ':)':         (":)",                     'bi/emoji-smile-fill-yellow.svg',         16, 16),
        'B)':         ("B)",                     'bi/emoji-sunglasses-fill-yellow.svg',        16, 16),
        ':))':        (":))",                    'bi/emoji-laughing-fill-yellow.svg',        16, 16),
        ';)':         (";)",                     'bi/emoji-wink-fill-yellow.svg',        16, 16),
        '/!\\':       ("/!\\",                   'bi/exclamation-triangle-red.svg',         16, 16),
        '<!>':        ("<!>",                    'bi/exclamation-circle.svg',     16, 16),
        '(!)':        ("(!)",                    'bi/lightbulb.svg',          16, 16),
        ':-?':        (":-?",                    'tongue.png',        16, 16),
        ':\\':        (":\\",                    'ohwell.png',        16, 16),
        '>:>':        (">:>",                    'devil.png',         16, 16),
        '|)':         ("|)",                     'bi/emoji-expressionless-fill-yellow.svg',         16, 16),
        ':-(':        (":-(",                    'bi/emoji-frown-fill-yellow.svg',           16, 16),
        ':-)':        (":-)",                    'bi/emoji-smile-fill-yellow.svg',         16, 16),
        'B-)':        ("B-)",                    'bi/emoji-sunglasses-fill-yellow.svg',        16, 16),
        ':-))':       (":-))",                   'bi/emoji-laughing-fill-yellow.svg',        16, 16),
        ';-)':        (";-)",                    'bi/emoji-wink-fill-yellow.svg',        16, 16),
        '|-)':        ("|-)",                    'bi/emoji-expressionless-fill-yellow.svg',         16, 16),
        '(./)':       ("(./)",                   'bi/check-circle-green.svg',     16, 16),
        '{OK}':       ("{OK}",                   'bi/hand-thumbs-up.svg',     16, 16),
        '{X}':        ("{X}",                    'bi/x-circle-red.svg',    16, 16),
        '{i}':        ("{i}",                    'bi/info-circle.svg',     16, 16),
        '{1}':        ("{1}",                    'prio1.png',         15, 13),
        '{2}':        ("{2}",                    'prio2.png',         15, 13),
        '{3}':        ("{3}",                    'prio3.png',         15, 13),
        '{*}':        ("{*}",                    'bi/star-fill.svg',       16, 16),
        '{o}':        ("{o}",                    'bi/star.svg',      16, 16),
    }
    del _

    stylesheets = (
        # media         basename
        ('all',         'bootstrap.min'),
        ('all',         '../fonts/bootstrap-icons'),
        ('all',         'moinizer'),
        ('all',         'ekladde'),

    )
    stylesheets_print = (
        ('all',         'bootstrap.min'),
        ('all',         '../fonts/bootstrap-icons'),
        ('all',         'moinizer'),
        ('all',         'ekladde'),
        ('all',         'memoprint'),
    )
    stylesheets_projection = (
        ('all',         'bootstrap.min'),
        ('all',         '../fonts/bootstrap-icons'),
        ('all',         'moinizer'),
        ('all',         'ekladde'),
        ('all',         'memoslide'),
    )


    html_logo = u'''
<nav id="document" class="navbar navbar-expand-lg navbar-light">
    <div class="container-fluid">
        <ul class="navbar-nav navbar-expand-lg me-auto">
            <li id="documentinfo" class="nav-item me-auto">
                <ul>
                %(document_info)s
                </ul>
            </li>
        </ul>

        <span class="nav-item d-flex">
          %(editbutton)s
        </span>

        <span class="nav-item dropdown">
          %(page_menu)s
        </span>

        <span class="nav-item">
          %(commentbutton)s
        </span>

      </ul>
  </div>
</nav>
'''

    html_nav_bar = u'''
<!-- ekladde.py header() START -->
<nav id="banner" class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <div class="container-fluid">
        <a class="navbar-brand col-md-3 col-lg-2" href="#">
            <!-- Sitename -->
            %(sitename)s
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div id="navbarCollapse" class="collapse navbar-collapse">

          <!-- Add form -->
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
            %(new_page)s
            </li>
          </ul>

          <!-- Search form -->
          %(search)s

          <ul class="navbar-nav">
            <li class="nav-item dropdown">
                <!-- Menu -->
                %(menu_global)s
            </li> <!-- global menu .navbar-nav -->

            <!-- menu user logout dropdown -->
            <li class="nav-item dropdown">
                %(menu_user)s
            </li><!-- menu user .navbar-nav -->

          </ul>
        </div> <!-- id= navbarCollapse -->
    </div> <!--div container fluid -->
</nav>

<!-- Main container and row -->
<div class="container-fluid">
    <div id="content-row" class="row">
'''

    html_with_sidebar = u'''
            <!-- LEFT SIDEBAR -->
            <nav id="sidebar" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
                <div class="position-sticky pt-3">
                    <!-- SideBar contents -->
                    %(sidebar)s
                    <!-- Navilinks -->
                    %(navilinks)s
                    <!-- Trails -->
                    %(trail)s
                </div> <!-- position-sticky -->
            </nav> <!-- sidebar end -->
            %(custom_pre)s

            <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                <div class="doc_border w-100">
                    %(custom_post)s
                    %(msg)s
                    %(document_title_controls)s
    <!-- ekladde.py header() STOP -->
    <!-- Page contents -->
'''

    html_no_sidebar = u'''
            %(custom_pre)s
            <main class="ms-sm-auto px-md-4">
                <div class="doc_border w-100">
                    %(custom_post)s
                    %(msg)s
                    %(document_title_controls)s
    <!-- ekladde.py header() STOP -->
    <!-- Page contents -->
'''

    html_header = html_nav_bar + html_with_sidebar
    html_header_no_sidebar = html_nav_bar + html_no_sidebar

    html_new_page = u'''
        <form class="me-auto" method="POST" action="/%(page)s">
            <div class="input-group">
                    <input type="hidden" name="action" value="newpage">
                    <input type="hidden" name="parent" value="%(page)s">
                    <input type="hidden" name="template" value="">
                    <input type="hidden" name="nametemplate" value="%(placeholder)s">
                    <input type="text" name="pagename" placeholder="Sub page" id="add-input" class="form-control" aria-label="Text input to add a sub page.">
                    <button id="add-button" class="btn btn-primary" type="submit">Add</button>
            </div>
        </form>
'''
    html_drop_down_menu = u'''
      <!-- Dropdown menu -->
      <div class="dropdown">
        <button type="button" id="%(id)sDropDown" class="btn btn-outline-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            %(menu_name)s
        </button>
        <!-- Dropdown contents -->
        <ul class="dropdown-menu" aria-labelledby="%(id)sDropDown">
            %(menu_list)s
        </ul>
      </div>
      '''

    html_commentbutton = u'''
          <a href="#" class="menu-nav-comment nbcomment navbar-comment-toggle btn btn-outline-secondary" role="button" rel="nofollow" onClick="toggleComments();return false;" data-toggle="toggle" data-target=".navbar-comment-toggle"
                title="%(title)s">
            <span class="hidden-sm">%(comment)s</span>
          </a>
'''

    html_footer = u"""
<!-- End of page contents -->

      </div> <!-- /doc_border -->
    </main>
  </div> <!-- /row -->
</div> <!-- /container-fluid -->

  %(custom_pre)s

  <!-- Footer -->
  <div id="footer" class="row">
    <div class="offset-md-3 col-md-9 offset-lg-2 col-lg-10 text-end text-muted">
      %(credits)s
      %(version)s
      %(custom_post)s
    </div>
  </div>
  <!-- End of footer -->

  <!-- Bootstrap core JavaScript -->
  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
  <script src="%(prefix)s/%(theme)s/js/jquery.min.js"></script>
  <!-- Include all compiled plugins (below), or include individual files as needed -->
  <script src="%(prefix)s/%(theme)s/js/bootstrap.bundle.js"></script>
  <!-- toggle.js by dossist -->
  <script src="%(prefix)s/%(theme)s/js/toggle.js"></script>
  <script src="%(prefix)s/%(theme)s/js/ekladde.js"></script>
  <!-- Custom script -->
%(script)s
  <!-- End of JavaScript -->
"""

    #TODO i18n
    html_editor_buttons = u'''
    <div id="edit_controls">
        <button id="h1_button" class="btn btn-sm btn-secondary bi bi-type-h1" aria-label="H1 heading" data-toggle="tooltip" data-placement="top" title="H1 heading"></button>
        <button id="h2_button" class="btn btn-sm btn-secondary bi bi-type-h2" aria-label="H2 heading" data-toggle="tooltip" data-placement="top" title="H2 heading"></button>
        <button id="h3_button" class="btn btn-sm btn-secondary bi bi-type-h3" aria-label="H3 heading" data-toggle="tooltip" data-placement="top" title="H3 heading"></button>

        <button id="bold_button" class="btn btn-sm btn-secondary bi bi-type-bold" aria-label="Bold text formatting" data-toggle="tooltip" data-placement="top" title="Bold text formatting"></button>
        <button id="italic_button" class="btn btn-sm btn-secondary bi bi-type-italic" aria-label="Italic text formatting" data-toggle="tooltip" data-placement="top" title="Italic text formatting"></button>
        <button id="underline_button" class="btn btn-sm btn-secondary bi bi-type-underline" aria-label="Underline text formatting" data-toggle="tooltip" data-placement="top" title="Underline text formatting"></button>

        <button id="toc_button" class="btn btn-sm btn-secondary bi bi-list-nested" aria-label="Table of Content" data-toggle="tooltip" data-placement="top" title="Table of contents"></button>


        <button id="table_button" class="btn btn-sm btn-secondary bi bi-table" aria-label="Table insertion" data-toggle="tooltip" data-placement="top" title="Table insertion"></button>


        <button id="code_button" class="btn btn-sm btn-secondary bi bi-code-slash" aria-label="Code Formatting" data-toggle="tooltip" data-placement="top" title="Code formatting"></button>
        <button id="link_button" class="btn btn-sm btn-secondary bi bi-link-45deg" aria-label="Link Formatting"  data-toggle="tooltip" data-placement="top" title="Link formatting"></button>

    </div>
    '''

    html_script = ur"""
<script>
+function ($) {
// Toggle minified navbar under mobile landscape view
$('.navbar-collapse').on('show.bs.collapse', function () {
$('.navbar-mobile-toggle').togglejs('show');
});
$('.navbar-collapse').on('hidden.bs.collapse', function () {
$('.navbar-mobile-toggle').togglejs('hide');
});

//Scroll position fix for hash anchors
var mdAnchorFix = {
escapeRe: /[ !"#$%&'()*+,.\/:;<=>?@\[\\\]^`{|}~]/g,
escape: function (str) {
  return str.replace(mdAnchorFix.escapeRe, '\\$&');
},
rgbRe: /^rgba\(([ \t]*\d{1,3},){3}([ \t]*\d{1,3})\)$/i,
isTransparent: function (rgbstr) {
  if (rgbstr === 'transparent') {
    return true;
  }
  rgbMatch = rgbstr.match(mdAnchorFix.rgbRe);
  if (rgbMatch) {
    return (Number(rgbMatch[2]) ? false : true);
  }
  return false;
},
navbarHeight: function () {
  var height = 0;
  var $navbar = $('.navbar');
  if ( !mdAnchorFix.isTransparent($navbar.css('background-color'))
       && ($navbar.css('display') !== 'none')
       && ($navbar.css('visibility') !== 'hidden') ) {
    height = $navbar.height();
  }
  return height;
},
jump: function () {
  origin = $('#' + mdAnchorFix.escape(location.hash.substr(1))).offset().top;
  offset = mdAnchorFix.navbarHeight() + 15;
  setTimeout(function () { window.scrollTo(0, origin - offset); }, 1);
},
clickWrapper: function () {
  if ( ($(this).attr('href') === location.hash)
       || !('onhashchange' in window.document.body) ) {
    setTimeout(function () { $(window).trigger("hashchange"); }, 1);
  }
},
};
$('#pagebox a[href^="#"]:not([href="#"])').on("click", mdAnchorFix.clickWrapper);
$(window).on("hashchange", mdAnchorFix.jump);
if (location.hash) setTimeout(function () { mdAnchorFix.jump(); }, 100);
}(jQuery);
</script>
"""


    def header(self, d, **kw):
        """ Assemble wiki header
        header1: supported.
        header2: supported.

        @param d: parameter dictionary
        @rtype: unicode
        @return: page header html
        """
        if self.show_left_sidebar(d):
            template = self.html_header
        else:
            template = self.html_header_no_sidebar
        html = template % {'sitename': self.logo(),
       'document_title_controls': self.document_title_controls(d),
       'menu_global': self.menu_global(d),
       'new_page': self.new_page(d),
       'menu_user': self.menu_user(d),
       'search': self.searchform(d),
       'sidebar': self.sidebar(d),
       'trail': self.trail(d),
       'quicklinks': self.quicklinks(d),
       'navilinks': self.navibar(d),
       'msg': self.msg(d),
       'custom_pre': self.emit_custom_html(self.cfg.page_header1), # custom html just below the navbar, not recommended!
       'custom_post': self.emit_custom_html(self.cfg.page_header2), # custom html just before the contents, not recommended!
      }
        return html

    def new_page(self, d, **keywords):
        html = self.html_new_page % {'page': d['page'].split_title(), 'placeholder': '%s'}
        return html

    def editorheader(self, d, **kw):
        """
        header() for edit mode. Just set edit mode flag and call self.header().
        """
        d['edit_mode'] = 1
        return self.header(d, **kw) + self.html_editor_buttons

    def editbar(self, d, **keywords):
        print "Called editbar"
        html = super().editbar(d, keywords)
        return html

    def footer(self, d, **keywords):
        """ Assemble wiki footer
        footer1: supported.
        footer2: supported.

        @param d: parameter dictionary
        @keyword ...:...
        @rtype: unicode
        @return: page footer html
        """

        buffer = StringIO.StringIO()
        self.request.redirect(buffer)
        self.request.redirect()

        page = d['page']

        html = self.html_footer % {'pageinfo': self.pageinfo(page),
       'custom_pre': self.emit_custom_html(self.cfg.page_footer1), # Pre footer custom html (not recommended!)
       'credits': self.credits(d),
       'version': self.showversion(d, **keywords),
       'custom_post': self.emit_custom_html(self.cfg.page_footer2), # In-footer custom html (not recommended!)
       'prefix': self.cfg.url_prefix_static,
       'theme': self.name,
       'script': self.script(),
      }

        return html

    def script(self):
        """
        Append in-html script at the bottom of the page body.
        """
        return self.html_script

    def logo(self):
        """ Assemble logo with link to front page
        Using <a> tag only instead of wrapping with div

        The logo may contain an image and or text or any html markup.
        Just note that everything is enclosed in <a> tag.

        @rtype: unicode
        @return: logo html
        """
        html = u''
        if self.cfg.logo_string:
            # page = wikiutil.getFrontPage(self.request)
            # html = page.link_to_raw(self.request, self.cfg.logo_string, css_class="navbar-brand")
            html = u'''%s''' % self.cfg.logo_string
        return html


    def show_left_sidebar(self, d):
        # return true if this is a normal document
        # e.g. the edit page is not a normal document
        # Editor could be checked via d['edit_mode']
        if self.is_normal_document(d):
            return True
        else:
            return False

    def document_title_controls(self, d):
        if not self.is_normal_document(d):
            return self.non_document_title(d)

        return self.html_logo % {
                'document_info': self.document_info(d),
                'editbutton': self.editbutton(d),
                'page_menu': self.page_menu(d),
                'commentbutton': self.commentbutton(), }

    def non_document_title(self, d):
        """ If this is no document page but e.g. a search page
        we have to use this function """
        return '<span id="document_name">%s</span>' % wikiutil.escape(d['title_text'])


    def is_normal_document(self, d):
        return d['title_text'] == d['page'].split_title()

    def document_breadcrumb_list(self, d):
        """ Assemble the breadcrumb for the document location

        @param d: parameter dictionary
        @rtype: string
        @return: title html
        """
        _ = self.request.getText
        content = []
        pagepath = ''
        segments = d['page_name'].split('/') # was: title_text
        for s in segments[:-1]:
            pagepath += s
            content.append('<li class="breadcrumb-item">%s</li>' % Page(self.request, pagepath).link_to(self.request, s))
            pagepath += '/'
        active_document_link = self.backlink(d['page'], d['page_name'], segments[-1])
        content.append(('<li class="breadcrumb-item  active">%s</li>') % active_document_link)
        return "".join(content)

    def document_name(self, d):
        document_path_parts = d['page_name'].split('/')
        return document_path_parts[-1]

    def document_info(self, d):
        """ Assemble document info area on top of the document actual content.
        Certain pages shouldn't have info area as it feels redundant.
        Location area is excluded in FrontPage by default.
        Config variable memodump_hidelocation will override the list of pages to have no location area.
        """
        html = u''
        page = d['page']
        pages_hide = [self.request.cfg.page_front_page, ]
        try:
            pages_hide = self.request.cfg.memodump_hidelocation
        except AttributeError:
            pass
        if not page.page_name in pages_hide:
            html = u'''
            %(interwiki)s
            <nav aria-label="breadcrumb">
                <ol class="breadcrumb">
                    %(document_breadcrumb_list)s
                </ol>
            </nav>
            <span id="document_name">
                %(document_name)s
            </span>
            <span class="lastupdate">
                %(lastupdate)s
            </span>
''' % { 'interwiki': self.interwiki(d),
        'document_name': self.document_name(d),
        'document_breadcrumb_list': self.document_breadcrumb_list(d),
        'lastupdate': self.lastupdate(d)}
        return html

    def interwiki(self, d):
        """ Assemble the interwiki name display, linking to page_front_page

        @param d: parameter dictionary
        @rtype: string
        @return: interwiki html
        """
        if self.request.cfg.show_interwiki:
            page = wikiutil.getFrontPage(self.request)
            text = self.request.cfg.interwikiname or 'Self'
            link = page.link_to(self.request, text=text, rel='nofollow')
            html = u'<span id="interwiki">%s<span class="sep">:</span></span>' % link
        else:
            html = u''
        return html

    def lastupdate(self, d):
        """ Return html for last update in document info area, if conditions are met. """
        _ = self.request.getText
        page = d['page']
        html = u''
        if self.shouldShowPageinfo(page):
            info = page.lastEditInfo()
            if info:
                html = _('last modified %(time)s')
                html = html % {'time': info['time']}
        return html

    def searchform(self, d):
        """
        assemble HTML code for the search form

        @param d: parameter dictionary
        @rtype: unicode
        @return: search form html
        """
        _ = self.request.getText
        form = self.request.values
        updates = {
            'search_label': _('Search:'),
            'search_hint': _('Search'),
            'search_value': wikiutil.escape(form.get('value', ''), 1),
            'search_full_label': _('Text'),
            'search_title_label': _('Titles'),
            'url': self.request.href(d['page'].page_name)
        }
        d.update(updates)

        html = u'''
                <form class="d-flex" role="search" id="searchform" method="get" action="%(url)s">
                    <input type="hidden" name="action" value="fullsearch">
                    <input type="hidden" name="context" value="180">
                    <div class="input-group">
                        <input type="search" name="value" placeholder="%(search_hint)s" id="search-input" class="form-control" aria-label="%(search_hint)s">
                        <button id="search-button" class="btn btn-primary" type="submit">%(search_label)s</button>
                    </div>
                </form>
''' % d
        return html

    def editbutton(self, d):
        """ Return an edit button html fragment.

        If the user can't edit, return a disabled edit button.
        """
        page = d['page']

        if 'edit' in self.request.cfg.actions_excluded:
            return u""

        editlink_button = u''

        if not (page.isWritable() and
                self.request.user.may.write(page.page_name)):
            editlink_button = self.disabledEdit()
        else:
            _ = self.request.getText
            querystr = {'action': 'edit'}
            attrs = {'name': 'editlink', 'rel': 'nofollow', 'css_class': 'btn btn-outline-secondary', 'role': 'button', 'aria-disabled': 'true'}
            editlink_button = page.link_to_raw(self.request, text=_('edit'), querystr=querystr, **attrs)
        return editlink_button

    def disabledEdit(self):
        """ Return a disabled edit link """
        _ = self.request.getText
        html = u'%s<span class="hidden-sm">%s</span>%s' % (
                   self.request.formatter.url(1, css="btn btn-primary disabled"),
                   _('Immutable Page'),
                   self.request.formatter.url(0)
               )
        return html

    def commentbutton(self):
        """
        Return a comment toggle button html.
        Don't check if 'Comment' is present in self.request.cfg.edit_bar
        The button is display:none; (i.e. disappeared) by default, but will automatically appear
        when default javascript notices there is a comment in the source.
        """
        _ = self.request.getText
        html = self.html_commentbutton % {'comment': _('Comments'), 'title': _("Toggles visibility of comments in document.")}
        return html

    def menu_user(self, d):
        """ Assemble the username / userprefs link as dropdown menu
        Assemble a login link instead in case of no logged in user.

        @param d: parameter dictionary
        @rtype: unicode
        @return: username html
        """
        request = self.request
        _ = request.getText

        userlinks = []
        userbutton = u''
        loginbutton = u''

        # Add username/homepage link for registered users. We don't care
        # if it exists, the user can create it.
        if request.user.valid and request.user.name:
            interwiki = wikiutil.getInterwikiHomePage(request)
            name = request.user.name
            aliasname = request.user.aliasname
            if not aliasname:
                aliasname = name
            title = "%s @ %s" % (aliasname, interwiki[0])

            # link to (interwiki) user homepage
            wikitag, wikiurl, wikitail, wikitag_bad = wikiutil.resolve_interwiki(self.request, *interwiki)
            wikiurl = wikiutil.mapURL(self.request, wikiurl)
            href = wikiutil.join_wiki(wikiurl, wikitail)
            homelink = (request.formatter.url(1, href, title=title, css='dropdown-item bi-person-circle', rel="nofollow") +
                       request.formatter.text(name) +
                       request.formatter.url(0))
            userlinks.append(homelink)

            # link to userprefs action
            if 'userprefs' not in self.request.cfg.actions_excluded:
                userlinks.append(d['page'].link_to_raw(request, text=_('Settings'), css_class='dropdown-item bi-gear',
                                                       querystr={'action': 'userprefs'}, rel='nofollow'))
            # logout link
            if request.user.auth_method in request.cfg.auth_can_logout:
                userlinks.append(d['page'].link_to_raw(request, text=_('Logout'), css_class='dropdown-item bi-box-arrow-right',
                                                       querystr={'action': 'logout', 'logout': 'logout'}, rel='nofollow'))
            menu_list = u''
            for page_link in userlinks:
                menu_list += u'''<li>%(link)s</li>
''' % {'link': page_link}
            return self.drop_down_menu(name, menu_list, 'User')
        else:
            query = {'action': 'login'}
            # special direct-login link if the auth methods want no input
            if request.cfg.auth_login_inputs == ['special_no_input']:
                query['login'] = '1'
            if request.cfg.auth_have_login:
                loginbutton = (d['page'].link_to_raw(request, text=_("Login"),
                                                     querystr=query, css_class='menu-nav-login', rel='nofollow'))

            html = u'''
            <li>
              %s
            </li>
''' % loginbutton
            return html

        return u''


    def menu_global(self, d):
        """ The menu for non page related global functions
        """
        request = self.request
        try:
            menu_entries = request.cfg.memodump_menuoverride
        except AttributeError:
            # default list of items in dropdown menu.
            # menu items are assembled in this order.
            # see wiki for detailed info on customization.
            menu_entries = [
                '===== Navigation =====',
                'RecentChanges',
                'FindPage',
                'LocalSiteMap',
                '__separator__',
                '===== Edit =====',
                'editSideBar',
                '__separator__',
                '===== Help =====',
                'HelpContents',
                'HelpOnMoinWikiSyntax',
            ]

        menu_html_list = self._menu(d, menu_entries)
        _ = request.getText

        return self.drop_down_menu(_('Menu'), menu_html_list, 'Menu')

    def page_menu(self, d):
        """ The menu for content page related functions
        """
        request = self.request
        try:
            menu_entries = request.cfg.memodump_menuoverride
        except AttributeError:
            # default list of items in dropdown menu.
            # menu items are assembled in this order.
            # see wiki for detailed info on customization.
            menu_entries = [
                '===== Display =====',
                'AttachFile',
                'info',
                'raw',
                'print',
                '__separator__',
                '===== Edit =====',
                'RenamePage',
                'DeletePage',
                'revert',
                'CopyPage',
                'Load',
                'Save',
                'Despam',
                '__separator__',
                '===== User =====',
                'quicklink',
                'subscribe',
            ]

        menu_html_list = self._menu(d, menu_entries)
        _ = request.getText
        return self.drop_down_menu(_('Option'), menu_html_list, "Option")

    def drop_down_menu(self, name, menu_list, id=""):
        html = self.html_drop_down_menu % {'menu_name': name, 'menu_list': menu_list, 'id': id}
        return html

    def _menu(self, d, menu_entries):
        """
        Build dropdown menu html. Incompatible with original actionsMenu() method.

        Menu can be customized by adding a config variable 'memodump_menuoverride'.
        The variable will override the default menu set.
        Additional menu definitions are given via config method 'memodump_menu_def(request)'.
        See the code below or project wiki for details.

        @param d: parameter dictionary
        @rtype: string
        @return: menu html
        """
        request = self.request
        rev = request.rev
        page = d['page']
        _ = request.getText

        page_recent_changes = wikiutil.getLocalizedPage(request, u'RecentChanges')
        page_find_page = wikiutil.getLocalizedPage(request, u'FindPage')
        page_help_contents = wikiutil.getLocalizedPage(request, u'HelpContents')
        page_help_formatting = wikiutil.getLocalizedPage(request, u'HelpOnFormatting')
        page_help_wikisyntax = wikiutil.getLocalizedPage(request, u'HelpOnMoinWikiSyntax')
        page_title_index = wikiutil.getLocalizedPage(request, u'TitleIndex')
        page_word_index = wikiutil.getLocalizedPage(request, u'WordIndex')
        page_front_page = wikiutil.getFrontPage(request)
        page_sidebar = Page(request, request.getPragma('sidebar', u'SideBar'))
        quicklink = self.menuQuickLink(page)
        subscribe = self.menuSubscribe(page)


        # menu element definitions
        menu_def = {
            'raw': {
                # Title for this menu entry
                'title': _('Raw Text'),
                # href and args are for normal entries ('special': False), otherwise ignored.
                # 'href': Nonexistent or empty for current page
                'href': '',
                # 'args': {'query1': 'value1', 'query2': 'value2', }
                # Optionally specify this for <a href="href?query1=value1&query2=value2">
                # If href and args are both nonexistent or empty, key is automatically interpreted to be an action name
                # and href and args are automatically set.
                'args': '',
                # 'special' can be:
                #   'disabled', 'removed', 'separator' or 'header' for whatever they say,
                #    False, None or nonexistent for normal menu display.
                # 'separator' and 'header' are automatically removed when there are no entries to show among them.
                'special': False,
            },
            'print': {'title': _('Print View'), },
            'refresh': {
                'title': _('Delete Cache'),
                'special': not (self.memodumpIsAvailableAction(page, 'refresh') and page.canUseCache()) and 'removed',
            },
            'SpellCheck': {'title': _('Check Spelling'), },
            'RenamePage': {'title': _('Rename Page'), },
            'CopyPage':   {'title': _('Copy Page'), },
            'DeletePage': {'title': _('Delete Page'), },
            'LikePages':  {'title': _('Like Pages'), },
            'LocalSiteMap': {'title': _('Local Site Map'), },
            'MyPages':    {'title': _('My Pages'), },
            'SubscribeUser': {
                'title': _('Subscribe User'),
                'special': not (self.memodumpIsAvailableAction(page, 'SubscribeUser')
                                and request.user.may.admin(page.page_name)) and 'removed',
            },
            'Despam': {
                'title': _('Remove Spam'),
                'special': not (self.memodumpIsAvailableAction(page, 'Despam') and request.user.isSuperUser()) and 'removed',
            },
            'revert': {
                'title': _('Revert to this revision'),
                'special': not (self.memodumpIsAvailableAction(page, 'revert')
                                and rev
                                and request.user.may.revert(page.page_name)) and 'removed',
            },
            'PackagePages': {'title': _('Package Pages'), },
            'RenderAsDocbook': {'title': _('Render as Docbook'), },
            'SyncPages': {'title': _('Sync Pages'), },
            'AttachFile': {'title': _('Attachments'), },
            'quicklink': {
                'title': quicklink[1], 'args': dict(action=quicklink[0], rev=rev),
                'special': not quicklink[0] and 'removed',
            },
            'subscribe': {
                'title': subscribe[1], 'args': dict(action=subscribe[0], rev=rev),
                'special': not subscribe[0] and 'removed',
            },
            'info': {'title': _('Info'), },
# menu items not in menu_def will be assumed to be action names,
# and receive appropriate title, href, and args automatically.
#           'Load': {'title': _('Load'), },
#           'Save': {'title': _('Save'), },
            # menu decorations
            '__separator__':   {'title': _('------------------------'), 'special': 'separator', },
            '----':            {'title': _('------------------------'), 'special': 'separator', },
            '-----':           {'title': _('------------------------'), 'special': 'separator', },
            '------':          {'title': _('------------------------'), 'special': 'separator', },
            '-------':         {'title': _('------------------------'), 'special': 'separator', },
            '--------':        {'title': _('------------------------'), 'special': 'separator', },
            '---------':       {'title': _('------------------------'), 'special': 'separator', },
            '----------':      {'title': _('------------------------'), 'special': 'separator', },
            # header example
            '__title_navigation__': {'title': _('Navigation'), 'special': 'header', },
            # useful pages
            'RecentChanges':   {'title': page_recent_changes.page_name, 'href': page_recent_changes.url(request)},
            'FindPage':        {'title': page_find_page.page_name, 'href': page_find_page.url(request)},
            'HelpContents':    {'title': page_help_contents.page_name, 'href': page_help_contents.url(request)},
            'HelpOnFormatting': {'title': page_help_formatting.page_name, 'href': page_help_formatting.url(request)},
            'HelpOnMoinWikiSyntax': {'title': page_help_wikisyntax.page_name, 'href': page_help_wikisyntax.url(request)},
            'TitleIndex':      {'title': page_title_index.page_name, 'href': page_title_index.url(request)},
            'WordIndex':       {'title': page_word_index.page_name, 'href': page_word_index.url(request)},
            'FrontPage':       {'title': page_front_page.page_name, 'href': page_front_page.url(request)},
            'SideBar':         {'title': page_sidebar.page_name, 'href': page_sidebar.url(request)},
            'editSideBar': {
                'title': _('Edit SideBar'), 'href': page_sidebar.url(request),
                'args': dict(action='edit'),
                'special': not self.memodumpIsEditablePage(page_sidebar) and 'removed'
            },
        }

        # register state determining functions on request for use in config
        request.memodumpIsAvailableAction = self.memodumpIsAvailableAction
        request.memodumpIsEditablePage = self.memodumpIsEditablePage

        try:
            menu_def.update(request.cfg.memodump_menu_def(request))
        except AttributeError:
            pass

        compiled = self.menuCompile(d, menu_entries, menu_def)
        menubody = self.menuRender(compiled)

        if menubody:
            html = menubody
        else:
            html = u''

        return html

    def menuGetQueryString(self, args):
        """
        Return a URL query string generated from arguments dictionary.
        {'q1': 'v1', 'q2': 'v2'} will turn into u'?q1=val&q2=val'
        """
        parts = []
        for key, value in args.iteritems():
            if value:
                parts.append(u'%s=%s' % (key, value))
        output = u'&'.join(parts)
        if output:
            output = u'?' + output
        return output

    def menuCompile(self, d, menu, available_entries):
        """
        Return a compiled list of menu data ready to input to renderer.
        """
        # subroutines to generate compiled data
        def generateAction(action, title=''):
            query = self.menuGetQueryString({'action': action, 'rev': rev})
            if not title:
                title = _(action)
            return (action, title, u'%s%s' % (page.url(request), query), False)
        def generateHeader(key, title):
            return (key, _(title), '', 'header')
        def generateSpecial(key, data):
            return (key, data.get('title', _(key)), data.get('href', u''), data.get('special', False))
        def generateNormal(key, data):
            if not data.get('href'):
                data['href'] = page.url(request)
            if data.get('args'):
                data['href'] = u'%s%s' % (data['href'], self.menuGetQueryString(data['args']))
            return (key, data.get('title', _(key)), data.get('href'), False)

        request = self.request
        _ = request.getText
        rev = request.rev
        page = d['page']
        header_re = re.compile(r'^(\=+)\s+(.+?)\s+\1$') # '= title ='

        compiled = [] # [('key', 'title', 'href', 'special'), ]
        for key in menu:
            # check if key is in the definitions list
            data = available_entries.get(key)
            if data:
                # 'removed', 'disabled', 'separator' or 'header'
                if data.get('special'):
                    compiled.append(generateSpecial(key, data))
                # normal display
                else:
                    # recognizes key as action if href and args are not provided
                    if not (data.get('href') or data.get('args')):
                        if self.memodumpIsAvailableAction(page, key):
                            compiled.append(generateAction(key, title=data.get('title', '')))
                        else:
                            continue
                    # otherwise compile as a normal menu entry
                    else:
                        compiled.append(generateNormal(key, data))
            else:
                # check if key is header string
                header_match = header_re.search(key)
                # header
                if header_match:
                    compiled.append(generateHeader(key, header_match.group(2)))
                # action not in available_entries
                elif self.memodumpIsAvailableAction(page, key):
                    compiled.append(generateAction(key))

        return self.menuThinCompiled(compiled)

    def menuThinCompiled(self, compiled):
        """
        Remove unnecessary rules and headers as well as 'removed' items from compiled menu data.
        """
        how_nice = {
            False: 0,
            'header': 2,
            'separator': 1,
            'removed': 1000,
        }
        thinned = []
        atmosphere = how_nice['separator']

        for record in reversed(compiled):
            nice = how_nice.get(record[3], 0)
            if nice < atmosphere:
                thinned.append(record)
                atmosphere = nice
            if not nice:
                atmosphere = 1000

        thinned.reverse()
        return thinned

    def menuRender(self, compiled):
        templates = {
            False:       u'                <li><a href="%(href)s" class="dropdown-item menu-dd-%(key)s" rel="nofollow">%(title)s</a></li>',
            'disabled':  u'                <li class="disabled"><a href="#" class="dropdown-item menu-dd-%(key)s" rel="nofollow">%(title)s</a></li>',
            'separator': u'                <li class="border-top"></li>',
            'header':    u'                <li class="dropdown-header">%(title)s</li>',
            'removed':   u'',
        }

        lines = []
        for record in compiled:
            special = record[3]
            dictionary = dict(key=record[0], title=record[1], href=record[2])
            lines.append(templates[special] % dictionary)
        return u'\n'.join(lines)

    def memodumpIsAvailableAction(self, page, action):
        """
        Return if action is available or not.
        If action starts with lowercase, return True without actually check if action exists.
        """
        request = self.request
        excluded = request.cfg.actions_excluded
        available = get_available_actions(request.cfg, page, request.user)
        return not (action in excluded or (action[0].isupper() and not action in available))

    def memodumpIsEditablePage(self, page):
        """
        Return True if page is editable for current user, False if not.

        @param page: page object
        """
        return page.isWritable() and self.request.user.may.write(page.page_name)

    def menuQuickLink(self, page):
        """
        Return quicklink action name and localized text according to status of page

        @param page: page object
        @rtype: unicode
        @return (action, text)
        """
        if not self.request.user.valid:
            return (u'', u'')

        _ = self.request.getText
        if self.request.user.isQuickLinkedTo([page.page_name]):
            action, text = u'quickunlink', _("Remove Link")
        else:
            action, text = u'quicklink', _("Add Link")
        if action in self.request.cfg.actions_excluded:
            return (u'', u'')

        return (action, text)

    def menuSubscribe(self, page):
        """
        Return subscribe action name and localized text according to status of page

        @rtype: unicode
        @return (action, text)
        """
        if not ((self.cfg.mail_enabled or self.cfg.jabber_enabled) and self.request.user.valid):
            return (u'', u'')

        _ = self.request.getText
        if self.request.user.isSubscribedTo([page.page_name]):
            action, text = 'unsubscribe', _("Unsubscribe")
        else:
            action, text = 'subscribe', _("Subscribe")
        if action in self.request.cfg.actions_excluded:
            return (u'', u'')

        return (action, text)


    def sidebar(self, d, **keywords):
        """ Display page called SideBar as an additional element on every page
        content_id has been changed from the original

        @param d: parameter dictionary
        @rtype: string
        @return: sidebar html
        """

        # Check which page to display, return nothing if doesn't exist.
        sidebar = self.request.getPragma('sidebar', u'SideBar')
        page = Page(self.request, sidebar)
        if not page.exists():
            return u""
        # Capture the page's generated HTML in a buffer.
        buffer = StringIO.StringIO()
        self.request.redirect(buffer)
        try:
            page.send_page(content_only=1, content_id="sidebar-content")
        finally:
            self.request.redirect()
        return u'<div id="sidebar-content"  clearfix">%s</div>' % buffer.getvalue()

    def trail(self, d):
        """ Assemble page trail

        @param d: parameter dictionary
        @rtype: unicode
        @return: trail html
        """
        _ = self.request.getText
        request = self.request
        user = request.user
        html = u''
        li = u'                <li>%s</li>'

        if not user.valid or user.show_page_trail:
            trail = user.getTrail()
            if trail:
                items = []
                for pagename in trail:
                    try:
                        interwiki, page = wikiutil.split_interwiki(pagename)
                        if interwiki != request.cfg.interwikiname and interwiki != 'Self':
                            link = (self.request.formatter.interwikilink(True, interwiki, page) +
                                    self.shortenPagename(page) +
                                    self.request.formatter.interwikilink(False, interwiki, page))
                            items.append(li % link)
                            continue
                        else:
                            pagename = page

                    except ValueError:
                        pass
                    page = Page(request, pagename)
                    title = page.split_title()
                    title = self.shortenPagename(title)
                    link = page.link_to(request, title)
                    items.append(li % link)

                html = u'''
            <div id="pagetrail">
              <h4>%s</h4>
              <ul>
%s
              </ul>
            </div>
''' % (_('Trail'), u'\n'.join(items))

        return html

    def quicklinks(self, d):
        """ Assemble quicklinks

        @param d: parameter dictionary
        @rtype: unicode
        @return: quicklinks html
        """
        _ = self.request.getText
        html = u''
        li = u'                <li class="%s">%s</li>'
        found = {}
        items = []
        current = d['page_name']

        userlinks = self.request.user.getQuickLinks()
        for text in userlinks:
            # non-localized anchor and texts
            pagename, link = self.splitNavilink(text, localize=0)
            if not pagename in found:
                if pagename == current:
                    cls = 'userlink active'
                    link = u'<a>%s</a>' % pagename
                else:
                    cls = 'userlink'
                items.append(li % (cls, link))
                found[pagename] = 1

        if items:
            html = u'''
            <div id="quicklinks">
              <h4>%s</h4>
              <ul>
%s
              </ul>
            </div>
''' % (_('Quick links'), u'\n'.join(items))

        return html

    def navibar(self, d):
        """ Assemble the navibar (which moved to sidebar as one of sections)
        NavIbar, not the navbar at the page top!

        @param d: parameter dictionary
        @rtype: unicode
        @return: navibar html
        """
        request = self.request
        _ = request.getText
        found = {} # pages we found. prevent duplicates
        items = [] # navibar items
        item = u'                <li class="%s">%s</li>'
        current = d['page_name']

        # Process config navi_bar
        if request.cfg.navi_bar:
            for text in request.cfg.navi_bar:
                pagename, link = self.splitNavilink(text)
                if pagename == current:
                    cls = 'wikilink active'
                else:
                    cls = 'wikilink'
                items.append(item % (cls, link))
                found[pagename] = 1

        # Add user links to wiki links, eliminating duplicates.
        userlinks = request.user.getQuickLinks()
        for text in userlinks:
            # Split text without localization, user knows what he wants
            pagename, link = self.splitNavilink(text, localize=0)
            if not pagename in found:
                if pagename == current:
                    cls = 'userlink active'
                else:
                    cls = 'userlink'
                items.append(item % (cls, link))
                found[pagename] = 1

        # Add current page at end of local pages
#       if not current in found:
#           title = d['page'].split_title()
#           title = self.shortenPagename(title)
#           link = d['page'].link_to(request, title)
#           cls = 'active'
#           items.append(item % (cls, link))

        # Add sister pages.
        for sistername, sisterurl in request.cfg.sistersites:
            if sistername == request.cfg.interwikiname: # it is THIS wiki
                cls = 'sisterwiki active'
                items.append(item % (cls, sistername))
            else:
                # TODO optimize performance
                cache = caching.CacheEntry(request, 'sisters', sistername, 'farm', use_pickle=True)
                if cache.exists():
                    data = cache.content()
                    sisterpages = data['sisterpages']
                    if current in sisterpages:
                        cls = 'sisterwiki'
                        url = sisterpages[current]
                        link = request.formatter.url(1, url) + \
                               request.formatter.text(sistername) +\
                               request.formatter.url(0)
                        items.append(item % (cls, link))

        # Assemble html
        items = u''.join(items)
        html = u''
        if items:
            html = u'''
            <div>
              <h4>%s</h4>
              <ul id='navibar'>
%s
              </ul>
            </div>
''' % (_('Navigation'), items)

        return html

    def msg(self, d):
        """ Assemble the msg display

        Display a message in an alert box with an optional close button.

        @param d: parameter dictionary
        @rtype: unicode
        @return: msg display html
        """
        msgs = d['msg']
        if not msgs:
            return u''

        msg_switch = {
            'hint': {'alert_type': 'alert-success', 'icon': self.img_url('bi/lightbulb.svg')},
            'info': {'alert_type': 'alert-info',  'icon': self.img_url('bi/info-circle.svg')},
            'warning': {'alert_type': 'alert-warning', 'icon': self.img_url('bi/exclamation-circle.svg')},
            'error': {'alert_type': 'alert-danger', 'icon': self.img_url('bi/exclamation-triangle.svg')},
            'dialog': {'alert_type': 'alert-info', 'icon': self.img_url('bi/hand-index-thumb.svg')}
        }

        result = []
        template = u'''
        <div class="alert %(alert_type)s alert-dismissible d-flex align-items-center fade show" role="alert">
            <img class="bi flex-shrink-0 me-5" src="%(icon)s" width="24px" height="24px">
            <div>
            %(msg)s
            </div>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
'''
        for msg, msg_class in msgs:
            if msg_class in msg_switch:
                msg_text = None
                msg_attributes = msg_switch[msg_class]

                if hasattr(msg, 'render'):
                    msg_text = msg.render()
                else:
                    msg_text = msg

                if msg_text:
                    msg_attributes['msg'] = msg_text
                    if self.is_msg_wanted(msg_text):
                        result.append(template % msg_attributes)

        if result:
            return u'\n'.join(result)
        else:
            return u''

    def is_msg_wanted(self, msg_text):
        _ = self.request.getText
        if 'Other users will be <em>warned</em> until' in msg_text:
            return False
        if msg_text == _('Edit was cancelled.'):
            return False
        if msg_text == _('Thank you for your changes. Your attention to detail is appreciated.'):
            return False
        return True


    def send_title(self, text, **keywords):
        """ Capture original send_title() and rewrite DOCTYPE for html5 """

        # for mobile
        additional_head = u'<meta name="viewport" content="width=device-width,initial-scale=1.0">\n'
        try:
            if not self.request.cfg.memodump_additional_head:
                raise AttributeError
        except AttributeError:
            self.request.cfg.html_head = u'%s%s' % (additional_head, self.request.cfg.html_head)
            self.request.cfg.memodump_additional_head = True

        buffer = StringIO.StringIO()
        self.request.redirect(buffer)
        try:
            ThemeBase.send_title(self, text, **keywords)
        finally:
            self.request.redirect()
        html = re.sub(ur'^<!DOCTYPE HTML .*?>\n', ur'<!DOCTYPE html>\n', buffer.getvalue())
        self.request.write(html)

    # def guiEditorScript(self, d):
    #     """ Disable default skin javascript to prevent gui edit button from automatically appearing """
    #     return u''

    def _stylesheet_link(self, theme, media, href, title=None):
        """ Removed charset attribute to satisfy html5 requirements """
        if theme:
            href = '%s/%s/css/%s.css' % (self.cfg.url_prefix_static, self.name, href)
        attrs = 'type="text/css" media="%s" href="%s"' % (
                media, wikiutil.escape(href, True), )
        if title:
            return '<link rel="alternate stylesheet" %s title="%s">' % (attrs, title)
        else:
            return '<link rel="stylesheet" %s>' % attrs

def execute(request):
    """
    Generate and return a theme object

    @param request: the request object
    @rtype: MoinTheme
    @return: Theme object
    """
    return Theme(request)