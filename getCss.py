varNamesDark = {
    'COLOR_BACKGROUND_LIGHT': '#505F69',
    'COLOR_BACKGROUND_NORMAL': '#222c33',
    'COLOR_BACKGROUND_DARK': '#19232D',
    'COLOR_FOREGROUND_LIGHT': '#F0F0F0',
    'COLOR_FOREGROUND_NORMAL': '#AAAAAA',
    'COLOR_FOREGROUND_DARK': '#666565',
    'COLOR_SELECTION_LIGHT': '#148CD2',
    'COLOR_SELECTION_NORMAL': '#1464A0',
    'COLOR_SELECTION_DARK': '#14506E',
    'OPACITY_TOOLTIP': '230',
    'SIZE_BORDER_RADIUS': '4px',
    'W_STATUS_BAR_BACKGROUND_COLOR': '#182127',
    'COLOR_BORDER': '#19232D'
}

varNamesLight = {
    'COLOR_BACKGROUND_LIGHT': '#bfe1fd',
    'COLOR_BACKGROUND_NORMAL': '#dff0ff',
    'COLOR_BACKGROUND_DARK': '#eff7ff',
    'COLOR_FOREGROUND_LIGHT': '#222222',
    'COLOR_FOREGROUND_NORMAL': '#919191',
    'COLOR_FOREGROUND_DARK': '#d8d7d7',
    'COLOR_SELECTION_LIGHT': '#4db9fc',
    'COLOR_SELECTION_NORMAL': '#7fc6fc',
    'COLOR_SELECTION_DARK': '#8ed8fa',
    'OPACITY_TOOLTIP': '230',
    'SIZE_BORDER_RADIUS': '4px',
    'W_STATUS_BAR_BACKGROUND_COLOR': '#dfeffa',
    'COLOR_BORDER': '#d8d7d7'
}

# varNames.update({'BORDER_LIGHT' : '1px solid ' +  varNames['COLOR_BACKGROUND_LIGHT'] ,
# 'BORDER_NORMAL' : '1px solid ' +  varNames['COLOR_BACKGROUND_NORMAL'], 
# 'BORDER_DARK' : '1px solid ' +  varNames['COLOR_BACKGROUND_DARK'] ,
# 'BORDER_SELECTION_LIGHT' : '1px solid ' +  varNames['COLOR_SELECTION_LIGHT'] ,
# 'BORDER_SELECTION_NORMAL' : '1px solid ' +  varNames['COLOR_SELECTION_NORMAL'], 
# 'BORDER_SELECTION_DARK' : '1px solid ' +  varNames['COLOR_SELECTION_DARK'] })

# with open('vars.css') as f:
#     a = f.read()
# dark,light = a.replace('\n','').replace(' ','').split('*')[1:]
# varNamesDark = {}
# for x in dark[1:-2].split(';'):
#     varNamesDark.update({x.split(':')[0]:x.split(':')[1]})
# varNamesLight = {}
# for x in light[1:-2].split(';'):
#     varNamesLight.update({x.split(':')[0]:x.split(':')[1]})

def css(mode='light',res=728):
    varNames = varNamesDark if mode == 'dark' else varNamesLight
    if res<=728:
        varNames.update({'FONT_SIZE':'12px','STATUS_BAR_FONT':'18px'})
    else:
        varNames.update({'FONT_SIZE':'14px','STATUS_BAR_FONT':'20px'})
    cssDefault = '''
        *{
            font-family: Roboto, Ubuntu, sans-serif;
            font-size: FONT_SIZE;
        }
        QWidget {
            background-color: COLOR_BACKGROUND_DARK;
            border: 0px solid COLOR_BACKGROUND_NORMAL;
            padding: 0px;
            color: COLOR_FOREGROUND_LIGHT;
            selection-background-color: COLOR_SELECTION_NORMAL;
            selection-color: COLOR_FOREGROUND_LIGHT;
        }

        QWidget:disabled {
            background-color: COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_DARK;
            selection-background-color: COLOR_SELECTION_DARK;
            selection-color: COLOR_FOREGROUND_DARK;
        }

        QWidget::item:selected {
            background-color: COLOR_SELECTION_NORMAL;
        }

        QWidget::item:hover {
            background-color: COLOR_SELECTION_LIGHT;
            color: COLOR_BACKGROUND_NORMAL;
        }

        QMainWindow::separator {
            background-color: COLOR_BACKGROUND_NORMAL;
            border: 0px solid COLOR_BACKGROUND_DARK;
            spacing: 0px;
            padding: 2px;
        }

        QMainWindow::separator:hover {
            background-color: COLOR_BACKGROUND_LIGHT;
            border: 0px solid COLOR_SELECTION_LIGHT;
        }

        QMainWindow::separator:horizontal {
            width: 5px;
            margin-top: 2px;
            margin-bottom: 2px;
            image: url('./ico/rc/toolbar_separator_vertical.png');
        }

        QMainWindow::separator:vertical {
            height: 5px;
            margin-left: 2px;
            margin-right: 2px;
            image: url('./ico/rc/toolbar_separator_horizontal.png');
        }

        QToolTip {
            background-color: COLOR_SELECTION_LIGHT;
            border: 1px solid COLOR_BORDER;
            color: COLOR_BACKGROUND_DARK;
            /* Remove padding, for fix combo box tooltip */
            padding: 0px;
            /* Remove opacity, fix #174 - may need to use RGBA */
        }

        QStatusBar {
            font-size: STATUS_BAR_FONT;
            border: 1px solid COLOR_BORDER;
            /* Fixes Spyder #9120, #9121 */
            background: W_STATUS_BAR_BACKGROUND_COLOR;
            /* Fixes #205, white vertical borders separating items */
        }

        QStatusBar::item {
            border: none;
        }

        QStatusBar QToolTip {
            background-color: COLOR_SELECTION_LIGHT;
            border: 1px solid COLOR_BORDER;
            color: COLOR_BACKGROUND_DARK;
            /* Remove padding, for fix combo box tooltip */
            padding: 0px;
            /* Reducing transparency to read better */
            opacity: OPACITY_TOOLTIP;
        }

        QStatusBar QPushButton {
            background: COLOR_BACKGROUND_NORMAL;
            border: COLOR_BORDER;
            min-width: 0px;
            padding: 2px;
        }

        QCheckBox {
            background-color: COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_LIGHT;
            spacing: 4px;
            outline: none;
            padding-top: 4px;
            padding-bottom: 4px;
        }

        QCheckBox:focus {
            border: none;
        }

        QCheckBox QWidget:disabled {
            background-color: COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_DARK;
        }

        QCheckBox::indicator {
            margin-left: 4px;
            height: 16px;
            width: 16px;
        }

        QCheckBox::indicator:unchecked {
            image: url('./ico/rc/checkbox_unchecked.png');
        }

        QCheckBox::indicator:unchecked:hover,
        QCheckBox::indicator:unchecked:focus,
        QCheckBox::indicator:unchecked:pressed {
            border: none;
            image: url('./ico/rc/checkbox_unchecked_focus.png');
        }

        QCheckBox::indicator:unchecked:disabled {
            image: url('./ico/rc/checkbox_unchecked_disabled.png');
        }

        QCheckBox::indicator:checked {
            image: url('./ico/rc/checkbox_checked.png');
        }

        QCheckBox::indicator:checked:hover,
        QCheckBox::indicator:checked:focus,
        QCheckBox::indicator:checked:pressed {
            border: none;
            image: url('./ico/rc/checkbox_checked_focus.png');
        }

        QCheckBox::indicator:checked:disabled {
            image: url('./ico/rc/checkbox_checked_disabled.png');
        }

        QCheckBox::indicator:indeterminate {
            image: url('./ico/rc/checkbox_indeterminate.png');
        }

        QCheckBox::indicator:indeterminate:disabled {
            image: url('./ico/rc/checkbox_indeterminate_disabled.png');
        }

        QCheckBox::indicator:indeterminate:focus,
        QCheckBox::indicator:indeterminate:hover,
        QCheckBox::indicator:indeterminate:pressed {
            image: url('./ico/rc/checkbox_indeterminate_focus.png');
        }

        QGroupBox {
            font-weight: bold;
            border: 1px solid COLOR_BORDER;
            border-radius: SIZE_BORDER_RADIUS;
            padding: 4px;
            margin-top: 16px;
        }

        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            left: 3px;
            padding-left: 3px;
            padding-right: 5px;
            padding-top: 8px;
            padding-bottom: 16px;
        }

        QGroupBox::indicator {
            margin-left: 2px;
            height: 16px;
            width: 16px;
        }

        QGroupBox::indicator:unchecked {
            border: none;
            image: url('./ico/rc/checkbox_unchecked.png');
        }

        QGroupBox::indicator:unchecked:hover,
        QGroupBox::indicator:unchecked:focus,
        QGroupBox::indicator:unchecked:pressed {
            border: none;
            image: url('./ico/rc/checkbox_unchecked_focus.png');
        }

        QGroupBox::indicator:unchecked:disabled {
            image: url('./ico/rc/checkbox_unchecked_disabled.png');
        }

        QGroupBox::indicator:checked {
            border: none;
            image: url('./ico/rc/checkbox_checked.png');
        }

        QGroupBox::indicator:checked:hover,
        QGroupBox::indicator:checked:focus,
        QGroupBox::indicator:checked:pressed {
            border: none;
            image: url('./ico/rc/checkbox_checked_focus.png');
        }

        QGroupBox::indicator:checked:disabled {
            image: url('./ico/rc/checkbox_checked_disabled.png');
        }

        QRadioButton {
            background-color: COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_LIGHT;
            spacing: 4px;
            padding: 0px;
            border: none;
            outline: none;
        }

        QRadioButton:focus {
            border: none;
        }

        QRadioButton:disabled {
            background-color: COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_DARK;
            border: none;
            outline: none;
        }

        QRadioButton QWidget {
            background-color: COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_LIGHT;
            spacing: 0px;
            padding: 0px;
            outline: none;
            border: none;
        }

        QRadioButton::indicator {
            border: none;
            outline: none;
            margin-left: 4px;
            height: 16px;
            width: 16px;
        }

        QRadioButton::indicator:unchecked {
            image: url('./ico/rc/radio_unchecked.png');
        }

        QRadioButton::indicator:unchecked:hover,
        QRadioButton::indicator:unchecked:focus,
        QRadioButton::indicator:unchecked:pressed {
            border: none;
            outline: none;
            image: url('./ico/rc/radio_unchecked_focus.png');
        }

        QRadioButton::indicator:unchecked:disabled {
            image: url('./ico/rc/radio_unchecked_disabled.png');
        }

        QRadioButton::indicator:checked {
            border: none;
            outline: none;
            image: url('./ico/rc/radio_checked.png');
        }

        QRadioButton::indicator:checked:hover,
        QRadioButton::indicator:checked:focus,
        QRadioButton::indicator:checked:pressed {
            border: none;
            outline: none;
            image: url('./ico/rc/radio_checked_focus.png');
        }

        QRadioButton::indicator:checked:disabled {
            outline: none;
            image: url('./ico/rc/radio_checked_disabled.png');
        }

        QMenuBar {
            background-color: COLOR_BACKGROUND_NORMAL;
            padding: 2px;
            border: 1px solid COLOR_BORDER;
            color: COLOR_FOREGROUND_LIGHT;
        }

        QMenuBar:focus {
            border: 1px solid COLOR_SELECTION_LIGHT;
        }

        QMenuBar::item {
            background: transparent;
            padding: 4px;
        }

        QMenuBar::item:selected {
            padding: 4px;
            background: transparent;
            border: 0px solid COLOR_BACKGROUND_NORMAL;
        }

        QMenuBar::item:pressed {
            padding: 4px;
            border: 0px solid COLOR_BACKGROUND_NORMAL;
            background-color: COLOR_SELECTION_LIGHT;
            color: COLOR_FOREGROUND_LIGHT;
            margin-bottom: 0px;
            padding-bottom: 0px;
        }

        QMenu {
            border: 0px solid COLOR_BACKGROUND_NORMAL;
            color: COLOR_FOREGROUND_LIGHT;
            margin: 0px;
        }

        QMenu::separator {
            height: 1px;
            background-color: COLOR_BACKGROUND_LIGHT;
            color: COLOR_FOREGROUND_LIGHT;
        }

        QMenu::icon {
            margin: 0px;
            padding-left: 8px;
        }

        QMenu::item {
            background-color: COLOR_BACKGROUND_NORMAL;
            padding: 4px 24px 4px 24px;
            /* Reserve space for selection border */
            border: 1px transparent COLOR_BACKGROUND_NORMAL;
        }

        QMenu::item:selected {
            color: COLOR_FOREGROUND_LIGHT;
        }

        QMenu::indicator {
            width: 12px;
            height: 12px;
            padding-left: 6px;
            /* non-exclusive indicator = check box style indicator (see QActionGroup::setExclusive) */
        }

        QMenu::indicator:non-exclusive:unchecked {
            image: url('./ico/rc/checkbox_unchecked.png');
        }

        QMenu::indicator:non-exclusive:unchecked:selected {
            image: url('./ico/rc/checkbox_unchecked_disabled.png');
        }

        QMenu::indicator:non-exclusive:checked {
            image: url('./ico/rc/checkbox_checked.png');
        }

        QMenu::indicator:non-exclusive:checked:selected {
            image: url('./ico/rc/checkbox_checked_disabled.png');
            /* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */
        }

        QMenu::indicator:exclusive:unchecked {
            image: url('./ico/rc/radio_unchecked.png');
        }

        QMenu::indicator:exclusive:unchecked:selected {
            image: url('./ico/rc/radio_unchecked_disabled.png');
        }

        QMenu::indicator:exclusive:checked {
            image: url('./ico/rc/radio_checked.png');
        }

        QMenu::indicator:exclusive:checked:selected {
            image: url('./ico/rc/radio_checked_disabled.png');
        }

        QMenu::right-arrow {
            margin: 5px;
            image: url('./ico/rc/arrow_right.png');
            height: 12px;
            width: 12px;
        }

        QAbstractItemView {
            alternate-background-color: COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_LIGHT;
            border: 1px solid COLOR_BORDER;
            border-radius: SIZE_BORDER_RADIUS;
        }

        QAbstractItemView QLineEdit {
            padding: 2px;
        }

        QAbstractScrollArea {
            background-color: COLOR_BACKGROUND_DARK;
            border: 1px solid COLOR_BORDER;
            border-radius: SIZE_BORDER_RADIUS;
            padding: 2px;
            /* fix #159 */
            min-height: 1.25em;
            /* fix #159 */
            color: COLOR_FOREGROUND_LIGHT;
        }

        QAbstractScrollArea:disabled {
            color: COLOR_FOREGROUND_DARK;
        }

        QScrollArea QWidget QWidget:disabled {
            background-color: COLOR_BACKGROUND_DARK;
        }

        QScrollBar:horizontal {
            height: 16px;
            margin: 2px 16px 2px 16px;
            border: 1px solid COLOR_BORDER;
            border-radius: SIZE_BORDER_RADIUS;
            background-color: COLOR_BACKGROUND_DARK;
        }

        QScrollBar:vertical {
            background-color: COLOR_BACKGROUND_DARK;
            width: 16px;
            margin: 16px 2px 16px 2px;
            border: 1px solid COLOR_BORDER;
            border-radius: SIZE_BORDER_RADIUS;
        }

        QScrollBar::handle:horizontal {
            background-color: COLOR_FOREGROUND_DARK;
            border: 1px solid COLOR_BORDER;
            border-radius: 3px;
            min-width: 8px;
        }

        QScrollBar::handle:horizontal:hover {
            background-color: COLOR_SELECTION_LIGHT;
            border: 1px solid COLOR_SELECTION_LIGHT;
            min-width: 8px;
        }

        QScrollBar::handle:horizontal:focus {
            border: 1px solid COLOR_SELECTION_NORMAL;
        }

        QScrollBar::handle:vertical {
            background-color: COLOR_FOREGROUND_DARK;
            border: 1px solid COLOR_BORDER;
            min-height: 8px;
            border-radius: 3px;
        }

        QScrollBar::handle:vertical:hover {
            background-color: COLOR_SELECTION_LIGHT;
            border: 1px solid COLOR_SELECTION_LIGHT;
            min-height: 8px;
        }

        QScrollBar::handle:vertical:focus {
            border: 1px solid COLOR_SELECTION_NORMAL;
        }

        QScrollBar::add-line:horizontal {
            margin: 0px 0px 0px 0px;
            border-image: url('./ico/rc/arrow_right_disabled.png');
            height: 12px;
            width: 12px;
            subcontrol-position: right;
            subcontrol-origin: margin;
        }

        QScrollBar::add-line:horizontal:hover,
        QScrollBar::add-line:horizontal:on {
            border-image: url('./ico/rc/arrow_right.png');
            height: 12px;
            width: 12px;
            subcontrol-position: right;
            subcontrol-origin: margin;
        }

        QScrollBar::add-line:vertical {
            margin: 3px 0px 3px 0px;
            border-image: url('./ico/rc/arrow_down_disabled.png');
            height: 12px;
            width: 12px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }

        QScrollBar::add-line:vertical:hover,
        QScrollBar::add-line:vertical:on {
            border-image: url('./ico/rc/arrow_down.png');
            height: 12px;
            width: 12px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }

        QScrollBar::sub-line:horizontal {
            margin: 0px 3px 0px 3px;
            border-image: url('./ico/rc/arrow_left_disabled.png');
            height: 12px;
            width: 12px;
            subcontrol-position: left;
            subcontrol-origin: margin;
        }

        QScrollBar::sub-line:horizontal:hover,
        QScrollBar::sub-line:horizontal:on {
            border-image: url('./ico/rc/arrow_left.png');
            height: 12px;
            width: 12px;
            subcontrol-position: left;
            subcontrol-origin: margin;
        }

        QScrollBar::sub-line:vertical {
            margin: 3px 0px 3px 0px;
            border-image: url('./ico/rc/arrow_up_disabled.png');
            height: 12px;
            width: 12px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }

        QScrollBar::sub-line:vertical:hover,
        QScrollBar::sub-line:vertical:on {
            border-image: url('./ico/rc/arrow_up.png');
            height: 12px;
            width: 12px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }

        QScrollBar::up-arrow:horizontal,
        QScrollBar::down-arrow:horizontal {
            background: none;
        }

        QScrollBar::up-arrow:vertical,
        QScrollBar::down-arrow:vertical {
            background: none;
        }

        QScrollBar::add-page:horizontal,
        QScrollBar::sub-page:horizontal {
            background: none;
        }

        QScrollBar::add-page:vertical,
        QScrollBar::sub-page:vertical {
            background: none;
        }

        QTextEdit {
            background-color: COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_LIGHT;
            border-radius: SIZE_BORDER_RADIUS;
            border: 1px solid COLOR_BORDER;
        }

        QTextEdit:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
            color: COLOR_FOREGROUND_LIGHT;
        }

        QTextEdit:focus {
            border: 1px solid COLOR_SELECTION_NORMAL;
        }

        QTextEdit:selected {
            background: COLOR_SELECTION_NORMAL;
            color: COLOR_BACKGROUND_NORMAL;
        }

        QPlainTextEdit {
            background-color: COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_LIGHT;
            border-radius: SIZE_BORDER_RADIUS;
            border: 1px solid COLOR_BORDER;
        }

        QPlainTextEdit:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
            color: COLOR_FOREGROUND_LIGHT;
        }

        QPlainTextEdit:focus {
            border: 1px solid COLOR_SELECTION_NORMAL;
        }

        QPlainTextEdit:selected {
            background: COLOR_SELECTION_NORMAL;
            color: COLOR_BACKGROUND_NORMAL;
        }

        QSizeGrip {
            background: transparent;
            width: 12px;
            height: 12px;
            image: url('./ico/rc/window_grip.png');
        }

        QStackedWidget {
            padding: 2px;
            border: 1px solid COLOR_BORDER;
            border: 1px solid COLOR_BORDER;
        }

        QToolBar {
            background-color: COLOR_BACKGROUND_NORMAL;
            border-bottom: 1px solid COLOR_BORDER;
            padding: 2px;
            font-weight: bold;
            spacing: 2px;
        }

        QToolBar QToolButton {
            background-color: COLOR_BACKGROUND_NORMAL;
            border: 0px solid COLOR_FOREGROUND_DARK;
        }

        QToolBar QToolButton:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
        }

        QToolBar QToolButton:checked {
            border: 1px solid COLOR_BORDER;
            background-color: COLOR_BACKGROUND_LIGHT;
        }

        QToolBar QToolButton:checked:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
        }

        QToolBar::handle:horizontal {
            width: 16px;
            image: url('./ico/rc/toolbar_move_horizontal.png');
        }

        QToolBar::handle:vertical {
            height: 16px;
            image: url('./ico/rc/toolbar_move_vertical.png');
        }

        QToolBar::separator:horizontal {
            width: 16px;
            image: url('./ico/rc/toolbar_separator_horizontal.png');
        }

        QToolBar::separator:vertical {
            height: 16px;
            image: url('./ico/rc/toolbar_separator_vertical.png');
        }

        QToolButton#qt_toolbar_ext_button {
            background: COLOR_BACKGROUND_NORMAL;
            border: 0px;
            color: COLOR_FOREGROUND_LIGHT;
            image: url('./ico/rc/arrow_right.png');
        }

        QAbstractSpinBox {
            background-color: COLOR_BACKGROUND_DARK;
            border: 1px solid COLOR_BORDER;
            color: COLOR_FOREGROUND_LIGHT;
            /* This fixes 103, 111 */
            padding-top: 2px;
            /* This fixes 103, 111 */
            padding-bottom: 2px;
            padding-left: 4px;
            padding-right: 4px;
            border-radius: SIZE_BORDER_RADIUS;
            /* min-width: 5px; removed to fix 109 */
        }

        QAbstractSpinBox:up-button {
            background-color: transparent COLOR_BACKGROUND_DARK;
            subcontrol-origin: border;
            subcontrol-position: top right;
            border-left: 1px solid COLOR_BACKGROUND_NORMAL;
            border-bottom: 1px solid COLOR_BACKGROUND_NORMAL;
            border-top-left-radius: 0;
            border-bottom-left-radius: 0;
            margin: 1px;
            width: 12px;
            margin-bottom: -1px;
        }

        QAbstractSpinBox::up-arrow,
        QAbstractSpinBox::up-arrow:disabled,
        QAbstractSpinBox::up-arrow:off {
            image: url('./ico/rc/arrow_up_disabled.png');
            height: 8px;
            width: 8px;
        }

        QAbstractSpinBox::up-arrow:hover {
            image: url('./ico/rc/arrow_up.png');
        }

        QAbstractSpinBox:down-button {
            background-color: transparent COLOR_BACKGROUND_DARK;
            subcontrol-origin: border;
            subcontrol-position: bottom right;
            border-left: 1px solid COLOR_BACKGROUND_NORMAL;
            border-top: 1px solid COLOR_BACKGROUND_NORMAL;
            border-top-left-radius: 0;
            border-bottom-left-radius: 0;
            margin: 1px;
            width: 12px;
            margin-top: -1px;
        }

        QAbstractSpinBox::down-arrow,
        QAbstractSpinBox::down-arrow:disabled,
        QAbstractSpinBox::down-arrow:off {
            image: url('./ico/rc/arrow_down_disabled.png');
            height: 8px;
            width: 8px;
        }

        QAbstractSpinBox::down-arrow:hover {
            image: url('./ico/rc/arrow_down.png');
        }

        QAbstractSpinBox:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
            color: COLOR_FOREGROUND_LIGHT;
        }

        QAbstractSpinBox:focus {
            border: 1px solid COLOR_SELECTION_NORMAL;
        }

        QAbstractSpinBox:selected {
            background: COLOR_SELECTION_NORMAL;
            color: COLOR_BACKGROUND_NORMAL;
        }

        QLabel {
            background-color: none;
            border: none;
            padding: 2px;
            margin: 0px;
            color: COLOR_FOREGROUND_LIGHT;
        }

        QLabel:disabled {
            background-color: COLOR_BACKGROUND_DARK;
            border: 0px solid COLOR_BACKGROUND_NORMAL;
            color: COLOR_FOREGROUND_DARK;
        }

        QTextBrowser {
            background-color: COLOR_BACKGROUND_DARK;
            border: 1px solid COLOR_BORDER;
            color: COLOR_FOREGROUND_LIGHT;
            border-radius: SIZE_BORDER_RADIUS;
        }

        QTextBrowser:disabled {
            background-color: COLOR_BACKGROUND_DARK;
            border: 1px solid COLOR_BORDER;
            color: COLOR_FOREGROUND_DARK;
            border-radius: SIZE_BORDER_RADIUS;
        }

        QTextBrowser:hover,
        QTextBrowser:!hover,
        QTextBrowser:selected,
        QTextBrowser:pressed {
            border: 1px solid COLOR_BORDER;
        }

        QGraphicsView {
            background-color: COLOR_BACKGROUND_DARK;
            border: 1px solid COLOR_BORDER;
            color: COLOR_FOREGROUND_LIGHT;
            border-radius: SIZE_BORDER_RADIUS;
        }

        QGraphicsView:disabled {
            background-color: COLOR_BACKGROUND_DARK;
            border: 1px solid COLOR_BORDER;
            color: COLOR_FOREGROUND_DARK;
            border-radius: SIZE_BORDER_RADIUS;
        }

        QGraphicsView:hover,
        QGraphicsView:!hover,
        QGraphicsView:selected,
        QGraphicsView:pressed {
            border: 1px solid COLOR_BORDER;
        }

        QCalendarWidget {
            border: 1px solid COLOR_BORDER;
            border-radius: SIZE_BORDER_RADIUS;
        }

        QCalendarWidget:disabled {
            background-color: COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_DARK;
        }

        QLCDNumber {
            background-color: COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_LIGHT;
        }

        QLCDNumber:disabled {
            background-color: COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_DARK;
        }

        QProgressBar {
            background-color: COLOR_BACKGROUND_DARK;
            border: 1px solid COLOR_BORDER;
            color: COLOR_FOREGROUND_LIGHT;
            border-radius: SIZE_BORDER_RADIUS;
            text-align: right;
            padding-right: 3px;
        }

        QProgressBar:disabled {
            background-color: COLOR_BACKGROUND_DARK;
            border: 1px solid COLOR_BORDER;
            color: COLOR_FOREGROUND_DARK;
            border-radius: SIZE_BORDER_RADIUS;
            text-align: center;
        }

        QProgressBar::chunk {
            background-color: COLOR_SELECTION_NORMAL;
            color: COLOR_BACKGROUND_DARK;
            border-radius: SIZE_BORDER_RADIUS;
        }

        QProgressBar::chunk:disabled {
            background-color: COLOR_SELECTION_DARK;
            color: COLOR_FOREGROUND_DARK;
            border-radius: SIZE_BORDER_RADIUS;
        }

        QPushButton {
            background-color: COLOR_BACKGROUND_LIGHT;
            border: none;
            color: COLOR_FOREGROUND_LIGHT;
            border-radius: SIZE_BORDER_RADIUS;
            padding: 3px;
            outline: none;
            /* Issue #194 - Special case of QPushButton inside dialogs, for better UI */
            min-width: 80px;
        }

        QPushButton:disabled {
            background-color: COLOR_BACKGROUND_NORMAL;
            border: none;
            color: COLOR_FOREGROUND_DARK;
            border-radius: SIZE_BORDER_RADIUS;
            padding: 3px;
        }

        QPushButton:checked {
            background-color: COLOR_BACKGROUND_NORMAL;
            border: none;
            border-radius: SIZE_BORDER_RADIUS;
            padding: 3px;
            outline: none;
        }

        QPushButton:checked:disabled {
            background-color: COLOR_BACKGROUND_DARK;
            border: none;
            color: COLOR_FOREGROUND_DARK;
            border-radius: SIZE_BORDER_RADIUS;
            padding: 3px;
            outline: none;
        }

        QPushButton:checked:selected {
            background: COLOR_SELECTION_NORMAL;
            color: COLOR_BACKGROUND_NORMAL;
        }

        QPushButton::menu-indicator {
            subcontrol-origin: padding;
            subcontrol-position: bottom right;
            bottom: 4px;
        }

        QPushButton:pressed {
            background-color: COLOR_BACKGROUND_DARK;
            border: 1px solid COLOR_BORDER;
        }

        QPushButton:pressed:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
        }

        QPushButton:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
            color: COLOR_FOREGROUND_LIGHT;
        }

        QPushButton:selected {
            background: COLOR_SELECTION_NORMAL;
            color: COLOR_BACKGROUND_NORMAL;
        }

        QPushButton:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
            color: COLOR_FOREGROUND_LIGHT;
        }

        QPushButton:focus {
            border: 1px solid COLOR_SELECTION_NORMAL;
        }

        QToolButton {
            background-color: transparent;
            border: none;
            border-radius: SIZE_BORDER_RADIUS;
            margin: 0px;
            padding: 2px;
        }

        QToolButton:checked {
            background-color: transparent;
            border: none;
        }

        QToolButton:checked:disabled {
            border: none;
        }

        QToolButton:pressed {
            margin: 1px;
            background-color: transparent;
            border: none;
        }

        QToolButton:disabled {
            border: none;
        }

        QToolButton:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
        }

        QToolButton[popupMode="0"] {
            /* Only for DelayedPopup */
            padding-right: 2px;
            /* The subcontrols below are used only in the MenuButtonPopup mode */
        }

        QToolButton[popupMode="1"] {
            /* Only for MenuButtonPopup */
            padding-right: 20px;
        }

        QToolButton[popupMode="1"]::menu-button {
            border: none;
        }

        QToolButton[popupMode="1"]::menu-button:hover {
            border: none;
            border-left: 1px solid COLOR_SELECTION_LIGHT;
            border-radius: 0;
            /* The subcontrol below is used only in the InstantPopup or DelayedPopup mode */
        }

        QToolButton[popupMode="2"] {
            /* Only for InstantPopup */
            padding-right: 2px;
        }

        QToolButton::menu-button {
            padding: 2px;
            border-radius: SIZE_BORDER_RADIUS;
            border: 1px solid COLOR_BORDER;
            width: 12px;
            outline: none;
        }

        QToolButton::menu-button:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
        }

        QToolButton::menu-button:checked:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
        }

        QToolButton::menu-indicator {
            image: url('./ico/rc/arrow_down.png');
            height: 8px;
            width: 8px;
            top: 0;
            /* Exclude a shift for better image */
            left: -2px;
            /* Shift it a bit */
        }

        QToolButton::menu-arrow {
            image: url('./ico/rc/arrow_down.png');
            height: 8px;
            width: 8px;
        }

        QToolButton::menu-arrow:hover {
            image: url('./ico/rc/arrow_down_focus.png');
        }

        QCommandLinkButton {
            background-color: transparent;
            border: 1px solid COLOR_BORDER;
            color: COLOR_FOREGROUND_LIGHT;
            border-radius: SIZE_BORDER_RADIUS;
            padding: 0px;
            margin: 0px;
        }

        QCommandLinkButton:disabled {
            background-color: transparent;
            color: COLOR_FOREGROUND_DARK;
        }

        QComboBox {
            border: 1px solid COLOR_BORDER;
            border-radius: SIZE_BORDER_RADIUS;
            selection-background-color: COLOR_SELECTION_NORMAL;
            padding-left: 4px;
            padding-right: 4px;
            /* 4 + 16*2 See scrollbar size */
            /* Fixes #103, #111 */
            min-height: 1.5em;
            /* padding-top: 2px;     removed to fix #132 */
            /* padding-bottom: 2px;  removed to fix #132 */
            /* min-width: 75px;      removed to fix #109 */
        }

        QComboBox QAbstractItemView {
            border: 1px solid COLOR_BORDER;
            border-radius: 0;
            background-color: COLOR_BACKGROUND_DARK;
            selection-background-color: COLOR_SELECTION_NORMAL;
        }

        QComboBox QAbstractItemView:hover {
            background-color: COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_LIGHT;
        }

        QComboBox QAbstractItemView:selected {
            background: COLOR_SELECTION_NORMAL;
            color: COLOR_BACKGROUND_NORMAL;
        }

        QComboBox QAbstractItemView:alternate {
            background: COLOR_BACKGROUND_DARK;
        }

        QComboBox:disabled {
            background-color: COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_DARK;
        }

        QComboBox:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
        }

        QComboBox:focus {
            border: 1px solid COLOR_SELECTION_NORMAL;
        }

        QComboBox:on {
            selection-background-color: COLOR_SELECTION_NORMAL;
            /* Needed to remove indicator - fix #132 */
        }

        QComboBox::indicator {
            border: none;
            border-radius: 0;
            background-color: transparent;
            selection-background-color: transparent;
            color: transparent;
            selection-color: transparent;
            /* Needed to remove indicator - fix #132 */
        }

        QComboBox::indicator:alternate {
            background: COLOR_BACKGROUND_DARK;
        }

        QComboBox::item:alternate {
            background: COLOR_BACKGROUND_DARK;
        }

        QComboBox::item:checked {
            font-weight: bold;
        }

        QComboBox::item:selected {
            border: 0px solid transparent;
        }

        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 12px;
            border-left: 1px solid COLOR_BACKGROUND_NORMAL;
        }

        QComboBox::down-arrow {
            image: url('./ico/rc/arrow_down_disabled.png');
            height: 8px;
            width: 8px;
        }

        QComboBox::down-arrow:on,
        QComboBox::down-arrow:hover,
        QComboBox::down-arrow:focus {
            image: url('./ico/rc/arrow_down.png');
        }
        
        QSlider:disabled {
            background: COLOR_BACKGROUND_DARK;
        }

        QSlider:focus {
            border: none;
        }

        QSlider::groove:horizontal {
            background: COLOR_BACKGROUND_NORMAL;
            border: 1px solid COLOR_BORDER;
            height: 4px;
            margin: 0px;
            border-radius: SIZE_BORDER_RADIUS;
        }

        QSlider::groove:vertical {
            background: COLOR_BACKGROUND_NORMAL;
            border: 1px solid COLOR_BORDER;
            width: 4px;
            margin: 0px;
            border-radius: SIZE_BORDER_RADIUS;
        }

        QSlider::add-page:vertical {
            background: COLOR_SELECTION_NORMAL;
            border: 1px solid COLOR_BORDER;
            width: 4px;
            margin: 0px;
            border-radius: SIZE_BORDER_RADIUS;
        }

        QSlider::add-page:vertical :disabled {
            background: COLOR_SELECTION_DARK;
        }

        QSlider::sub-page:horizontal {
            background: COLOR_SELECTION_NORMAL;
            border: 1px solid COLOR_BORDER;
            height: 4px;
            margin: 0px;
            border-radius: SIZE_BORDER_RADIUS;
        }

        QSlider::sub-page:horizontal:disabled {
            background: COLOR_SELECTION_DARK;
        }

        QSlider::handle:horizontal {
            background: COLOR_FOREGROUND_DARK;
            border: 1px solid COLOR_BORDER;
            width: 8px;
            height: 8px;
            margin: -8px 0px;
            border-radius: SIZE_BORDER_RADIUS;
        }

        QSlider::handle:horizontal:hover {
            background: COLOR_SELECTION_LIGHT;
            border: 1px solid COLOR_SELECTION_LIGHT;
        }

        QSlider::handle:horizontal:focus {
            border: 1px solid COLOR_SELECTION_NORMAL;
        }

        QSlider::handle:vertical {
            background: COLOR_FOREGROUND_DARK;
            border: 1px solid COLOR_BORDER;
            width: 8px;
            height: 8px;
            margin: 0 -8px;
            border-radius: SIZE_BORDER_RADIUS;
        }

        QSlider::handle:vertical:hover {
            background: COLOR_SELECTION_LIGHT;
            border: 1px solid COLOR_SELECTION_LIGHT;
        }

        QSlider::handle:vertical:focus {
            border: 1px solid COLOR_SELECTION_NORMAL;
        }

        QLineEdit {
            background-color: COLOR_BACKGROUND_DARK;
            padding-top: 2px;
            padding-bottom: 2px;
            padding-left: 4px;
            padding-right: 4px;
            border-style: solid;
            border: 1px solid COLOR_BORDER;
            border-radius: SIZE_BORDER_RADIUS;
            color: COLOR_FOREGROUND_LIGHT;
            min-height: 16px;
        }

        QLineEdit:disabled {
            background-color: COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_DARK;
        }

        QLineEdit:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
            color: COLOR_FOREGROUND_LIGHT;
        }

        QLineEdit:focus {
            border: 1px solid COLOR_SELECTION_NORMAL;
        }

        QLineEdit:selected {
            background-color: COLOR_SELECTION_NORMAL;
            color: COLOR_BACKGROUND_NORMAL;
        }

        QTabWidget {
            padding: 2px;
            selection-background-color: COLOR_BACKGROUND_NORMAL;
        }

        QTabWidget QWidget {
            /* Fixes #189 */
            border-radius: SIZE_BORDER_RADIUS;
        }

        QTabWidget::pane {
            border: 1px solid COLOR_BORDER;
            border-radius: SIZE_BORDER_RADIUS;
            margin: 0px;
            /* Fixes double border inside pane with pyqt5 */
            padding: 0px;
        }

        QTabWidget::pane:selected {
            background-color: COLOR_BACKGROUND_NORMAL;
            border: 1px solid COLOR_SELECTION_NORMAL;
        }


        /* QTabBar ----------------------------------------------------------------
        https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar
        --------------------------------------------------------------------------- */

        QTabBar {
            qproperty-drawBase: 0;
            border-radius: SIZE_BORDER_RADIUS;
            margin: 0px;
            padding: 2px;
            border: 0;
            /* left: 5px; move to the right by 5px - removed for fix */
        }

        QTabBar::close-button {
            border: 0;
            margin: 2px;
            padding: 2px;
            image: url('./ico/rc/window_close.png');
        }

        QTabBar::close-button:hover {
            image: url('./ico/rc/window_close_focus.png');
        }

        QTabBar::close-button:pressed {
            image: url('./ico/rc/window_close_pressed.png');
        }


        /* QTabBar::tab - selected ------------------------------------------------
        https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar
        --------------------------------------------------------------------------- */

        QTabBar::tab:top:selected:disabled {
            border-bottom: 3px solid COLOR_SELECTION_DARK;
            color: COLOR_FOREGROUND_DARK;
            background-color: COLOR_BACKGROUND_NORMAL;
        }

        QTabBar::tab:bottom:selected:disabled {
            border-top: 3px solid COLOR_SELECTION_DARK;
            color: COLOR_FOREGROUND_DARK;
            background-color: COLOR_BACKGROUND_NORMAL;
        }

        QTabBar::tab:left:selected:disabled {
            border-right: 3px solid COLOR_SELECTION_DARK;
            color: COLOR_FOREGROUND_DARK;
            background-color: COLOR_BACKGROUND_NORMAL;
        }

        QTabBar::tab:right:selected:disabled {
            border-left: 3px solid COLOR_SELECTION_DARK;
            color: COLOR_FOREGROUND_DARK;
            background-color: COLOR_BACKGROUND_NORMAL;
            /* !selected and disabled ----------------------------------------- */
        }

        QTabBar::tab:top:!selected:disabled {
            border-bottom: 3px solid COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_DARK;
            background-color: COLOR_BACKGROUND_DARK;
        }

        QTabBar::tab:bottom:!selected:disabled {
            border-top: 3px solid COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_DARK;
            background-color: COLOR_BACKGROUND_DARK;
        }

        QTabBar::tab:left:!selected:disabled {
            border-right: 3px solid COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_DARK;
            background-color: COLOR_BACKGROUND_DARK;
        }

        QTabBar::tab:right:!selected:disabled {
            border-left: 3px solid COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_DARK;
            background-color: COLOR_BACKGROUND_DARK;
            /* selected ------------------------------------------------------- */
        }

        QTabBar::tab:top:!selected {
            border-bottom: 2px solid COLOR_BACKGROUND_DARK;
            margin-top: 2px;
        }

        QTabBar::tab:bottom:!selected {
            border-top: 2px solid COLOR_BACKGROUND_DARK;
            margin-bottom: 3px;
        }

        QTabBar::tab:left:!selected {
            border-left: 2px solid COLOR_BACKGROUND_DARK;
            margin-right: 2px;
        }

        QTabBar::tab:right:!selected {
            border-right: 2px solid COLOR_BACKGROUND_DARK;
            margin-left: 2px;
        }

        QTabBar::tab:top {
            background-color: COLOR_BACKGROUND_NORMAL;
            color: COLOR_FOREGROUND_LIGHT;
            margin-left: 2px;
            padding-left: 4px;
            padding-right: 4px;
            padding-top: 2px;
            padding-bottom: 2px;
            min-width: 5px;
            border-bottom: 3px solid COLOR_BACKGROUND_NORMAL;
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
        }

        QTabBar::tab:top:selected {
            background-color: COLOR_BACKGROUND_LIGHT;
            color: COLOR_FOREGROUND_LIGHT;
            border-bottom: 3px solid COLOR_SELECTION_NORMAL;
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
        }

        QTabBar::tab:top:!selected:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
            border-bottom: 3px solid COLOR_SELECTION_LIGHT;
            /* Fixes spyder-ide/spyder#9766 */
            padding-left: 4px;
            padding-right: 4px;
        }

        QTabBar::tab:bottom {
            color: COLOR_FOREGROUND_LIGHT;
            border-top: 3px solid COLOR_BACKGROUND_NORMAL;
            background-color: COLOR_BACKGROUND_NORMAL;
            margin-left: 2px;
            padding-left: 4px;
            padding-right: 4px;
            padding-top: 2px;
            padding-bottom: 2px;
            border-bottom-left-radius: 3px;
            border-bottom-right-radius: 3px;
            min-width: 5px;
        }

        QTabBar::tab:bottom:selected {
            color: COLOR_FOREGROUND_LIGHT;
            background-color: COLOR_BACKGROUND_LIGHT;
            border-top: 3px solid COLOR_SELECTION_NORMAL;
            border-bottom-left-radius: 3px;
            border-bottom-right-radius: 3px;
        }

        QTabBar::tab:bottom:!selected:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
            border-top: 3px solid COLOR_SELECTION_LIGHT;
            /* Fixes spyder-ide/spyder#9766 */
            padding-left: 4px;
            padding-right: 4px;
        }

        QTabBar::tab:left {
            color: COLOR_FOREGROUND_LIGHT;
            background-color: COLOR_BACKGROUND_NORMAL;
            margin-top: 2px;
            padding-left: 2px;
            padding-right: 2px;
            padding-top: 4px;
            padding-bottom: 4px;
            border-top-left-radius: 3px;
            border-bottom-left-radius: 3px;
            min-height: 5px;
        }

        QTabBar::tab:left:selected {
            color: COLOR_FOREGROUND_LIGHT;
            background-color: COLOR_BACKGROUND_LIGHT;
            border-right: 3px solid COLOR_SELECTION_NORMAL;
        }

        QTabBar::tab:left:!selected:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
            border-right: 3px solid COLOR_SELECTION_LIGHT;
            padding: 0px;
        }

        QTabBar::tab:right {
            color: COLOR_FOREGROUND_LIGHT;
            background-color: COLOR_BACKGROUND_NORMAL;
            margin-top: 2px;
            padding-left: 2px;
            padding-right: 2px;
            padding-top: 4px;
            padding-bottom: 4px;
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
            min-height: 5px;
        }

        QTabBar::tab:right:selected {
            color: COLOR_FOREGROUND_LIGHT;
            background-color: COLOR_BACKGROUND_LIGHT;
            border-left: 3px solid COLOR_SELECTION_NORMAL;
        }

        QTabBar::tab:right:!selected:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
            border-left: 3px solid COLOR_SELECTION_LIGHT;
            padding: 0px;
        }

        QTabBar QToolButton {
            /* Fixes #136 */
            background-color: COLOR_BACKGROUND_NORMAL;
            height: 12px;
            width: 12px;
        }

        QTabBar QToolButton:pressed {
            background-color: COLOR_BACKGROUND_NORMAL;
        }

        QTabBar QToolButton:pressed:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
        }

        QTabBar QToolButton::left-arrow:enabled {
            image: url('./ico/rc/arrow_left.png');
        }

        QTabBar QToolButton::left-arrow:disabled {
            image: url('./ico/rc/arrow_left_disabled.png');
        }

        QTabBar QToolButton::right-arrow:enabled {
            image: url('./ico/rc/arrow_right.png');
        }

        QTabBar QToolButton::right-arrow:disabled {
            image: url('./ico/rc/arrow_right_disabled.png');
        }


        /* QDockWiget -------------------------------------------------------------
        --------------------------------------------------------------------------- */

        QDockWidget {
            outline: 1px solid COLOR_BACKGROUND_NORMAL;
            background-color: COLOR_BACKGROUND_DARK;
            border: 1px solid COLOR_BORDER;
            border-radius: SIZE_BORDER_RADIUS;
            titlebar-close-icon: url('./ico/rc/window_close.png');
            titlebar-normal-icon: url('./ico/rc/window_undock.png');
        }

        QDockWidget::title {
            /* Better size for title bar */
            padding: 6px;
            spacing: 4px;
            border: none;
            background-color: COLOR_BACKGROUND_NORMAL;
        }

        QDockWidget::close-button {
            background-color: COLOR_BACKGROUND_NORMAL;
            border-radius: SIZE_BORDER_RADIUS;
            border: none;
        }

        QDockWidget::close-button:hover {
            image: url('./ico/rc/window_close_focus.png');
        }

        QDockWidget::close-button:pressed {
            image: url('./ico/rc/window_close_pressed.png');
        }

        QDockWidget::float-button {
            background-color: COLOR_BACKGROUND_NORMAL;
            border-radius: SIZE_BORDER_RADIUS;
            border: none;
        }

        QDockWidget::float-button:hover {
            image: url('./ico/rc/window_undock_focus.png');
        }

        QDockWidget::float-button:pressed {
            image: url('./ico/rc/window_undock_pressed.png');
        }


        /* QTreeView QListView QTableView -----------------------------------------
        https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtreeview
        https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlistview
        https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtableview
        --------------------------------------------------------------------------- */

        QTreeView:branch:selected,
        QTreeView:branch:hover {
            background: url('./ico/rc/transparent.png');
        }

        QTreeView:branch:has-siblings:!adjoins-item {
            border-image: url('./ico/rc/branch_line.png') 0;
        }

        QTreeView:branch:has-siblings:adjoins-item {
            border-image: url('./ico/rc/branch_more.png') 0;
        }

        QTreeView:branch:!has-children:!has-siblings:adjoins-item {
            border-image: url('./ico/rc/branch_end.png') 0;
        }

        QTreeView:branch:has-children:!has-siblings:closed,
        QTreeView:branch:closed:has-children:has-siblings {
            border-image: none;
            image: url('./ico/rc/branch_closed.png');
        }

        QTreeView:branch:open:has-children:!has-siblings,
        QTreeView:branch:open:has-children:has-siblings {
            border-image: none;
            image: url('./ico/rc/branch_open.png');
        }

        QTreeView:branch:has-children:!has-siblings:closed:hover,
        QTreeView:branch:closed:has-children:has-siblings:hover {
            image: url('./ico/rc/branch_closed_focus.png');
        }

        QTreeView:branch:open:has-children:!has-siblings:hover,
        QTreeView:branch:open:has-children:has-siblings:hover {
            image: url('./ico/rc/branch_open_focus.png');
        }

        QTreeView::indicator:checked,
        QListView::indicator:checked {
            image: url('./ico/rc/checkbox_checked.png');
        }

        QTreeView::indicator:checked:hover,
        QListView::indicator:checked:hover,
        QTreeView::indicator:checked:focus,
        QListView::indicator:checked:focus,
        QTreeView::indicator:checked:pressed,
        QListView::indicator:checked:pressed {
            image: url('./ico/rc/checkbox_checked_focus.png');
        }

        QTreeView::indicator:unchecked,
        QListView::indicator:unchecked {
            image: url('./ico/rc/checkbox_unchecked.png');
        }

        QTreeView::indicator:unchecked:hover,
        QListView::indicator:unchecked:hover,
        QTreeView::indicator:unchecked:focus,
        QListView::indicator:unchecked:focus,
        QTreeView::indicator:unchecked:pressed,
        QListView::indicator:unchecked:pressed {
            image: url('./ico/rc/checkbox_unchecked_focus.png');
        }

        QTreeView::indicator:indeterminate,
        QListView::indicator:indeterminate {
            image: url('./ico/rc/checkbox_indeterminate.png');
        }

        QTreeView::indicator:indeterminate:hover,
        QListView::indicator:indeterminate:hover,
        QTreeView::indicator:indeterminate:focus,
        QListView::indicator:indeterminate:focus,
        QTreeView::indicator:indeterminate:pressed,
        QListView::indicator:indeterminate:pressed {
            image: url('./ico/rc/checkbox_indeterminate_focus.png');
        }

        QTreeView,
        QListView,
        QTableView,
        QColumnView {
            background-color: COLOR_BACKGROUND_DARK;
            border: 1px solid COLOR_BORDER;
            color: COLOR_FOREGROUND_LIGHT;
            gridline-color: COLOR_BACKGROUND_NORMAL;
            border-radius: SIZE_BORDER_RADIUS;
        }

        QTreeView:disabled,
        QListView:disabled,
        QTableView:disabled,
        QColumnView:disabled {
            background-color: COLOR_BACKGROUND_DARK;
            color: COLOR_FOREGROUND_DARK;
        }

        QTreeView:selected,
        QListView:selected,
        QTableView:selected,
        QColumnView:selected {
            background-color: COLOR_SELECTION_NORMAL;
            color: COLOR_BACKGROUND_NORMAL;
        }

        QTreeView:hover,
        QListView:hover,
        QTableView:hover,
        QColumnView:hover {
            background-color: COLOR_BACKGROUND_DARK;
            border: 1px solid COLOR_SELECTION_LIGHT;
        }

        QTreeView::item:pressed,
        QListView::item:pressed,
        QTableView::item:pressed,
        QColumnView::item:pressed {
            background-color: COLOR_SELECTION_NORMAL;
        }

        QTreeView::item:selected:hover,
        QListView::item:selected:hover,
        QTableView::item:selected:hover,
        QColumnView::item:selected:hover {
            background: COLOR_SELECTION_NORMAL;
            color: COLOR_BACKGROUND_DARK;
        }

        QTreeView::item:selected:active,
        QListView::item:selected:active,
        QTableView::item:selected:active,
        QColumnView::item:selected:active {
            background-color: COLOR_SELECTION_NORMAL;
        }

        QTreeView::item:!selected:hover,
        QListView::item:!selected:hover,
        QTableView::item:!selected:hover,
        QColumnView::item:!selected:hover {
            outline: 0;
            color: COLOR_SELECTION_LIGHT;
            background-color: COLOR_BACKGROUND_NORMAL;
        }

        QTableCornerButton::section {
            background-color: COLOR_BACKGROUND_DARK;
            border: 1px transparent COLOR_BACKGROUND_NORMAL;
            border-radius: 0px;
        }


        /* QHeaderView ------------------------------------------------------------
        https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qheaderview
        --------------------------------------------------------------------------- */

        QHeaderView {
            background-color: COLOR_BACKGROUND_NORMAL;
            border: 0px transparent COLOR_BACKGROUND_NORMAL;
            padding: 0px;
            margin: 0px;
            border-radius: 0px;
        }

        QHeaderView:disabled {
            background-color: COLOR_BACKGROUND_NORMAL;
            border: 1px transparent COLOR_BACKGROUND_NORMAL;
            padding: 2px;
        }

        QHeaderView::section {
            background-color: COLOR_BACKGROUND_NORMAL;
            color: COLOR_FOREGROUND_LIGHT;
            padding: 2px;
            border-radius: 0px;
            text-align: left;
        }

        QHeaderView::section:checked {
            color: COLOR_FOREGROUND_LIGHT;
            background-color: COLOR_SELECTION_NORMAL;
        }

        QHeaderView::section:checked:disabled {
            color: COLOR_FOREGROUND_DARK;
            background-color: COLOR_SELECTION_DARK;
        }

        QHeaderView::section::horizontal {
            padding-left: 4px;
            padding-right: 4px;
            border-left: 1px solid COLOR_BORDER;
        }

        QHeaderView::section::horizontal::first,
        QHeaderView::section::horizontal::only-one {
            border-left: 1px solid COLOR_BACKGROUND_NORMAL;
        }

        QHeaderView::section::horizontal:disabled {
            color: COLOR_FOREGROUND_DARK;
        }

        QHeaderView::section::vertical {
            padding-left: 4px;
            padding-right: 4px;
            border-top: 1px solid COLOR_BORDER;
        }

        QHeaderView::section::vertical::first,
        QHeaderView::section::vertical::only-one {
            border-top: 1px solid COLOR_BACKGROUND_NORMAL;
        }

        QHeaderView::section::vertical:disabled {
            color: COLOR_FOREGROUND_DARK;
        }

        QHeaderView::down-arrow {
            /* Those settings (border/width/height/background-color) solve bug */
            /* transparent arrow background and size */
            background-color: COLOR_BACKGROUND_NORMAL;
            border: none;
            height: 12px;
            width: 12px;
            padding-left: 2px;
            padding-right: 2px;
            image: url('./ico/rc/arrow_down.png');
        }

        QHeaderView::up-arrow {
            background-color: COLOR_BACKGROUND_NORMAL;
            border: none;
            height: 12px;
            width: 12px;
            padding-left: 2px;
            padding-right: 2px;
            image: url('./ico/rc/arrow_up.png');
        }


        /* QToolBox --------------------------------------------------------------
        https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbox
        --------------------------------------------------------------------------- */

        QToolBox {
            padding: 0px;
            border: 0px;
            border: 1px solid COLOR_BORDER;
        }

        QToolBox:selected {
            padding: 0px;
            border: 2px solid COLOR_SELECTION_NORMAL;
        }

        QToolBox::tab {
            background-color: COLOR_BACKGROUND_DARK;
            border: 1px solid COLOR_BORDER;
            color: COLOR_FOREGROUND_LIGHT;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
        }

        QToolBox::tab:disabled {
            color: COLOR_FOREGROUND_DARK;
        }

        QToolBox::tab:selected {
            background-color: COLOR_BACKGROUND_LIGHT;
            border-bottom: 2px solid COLOR_SELECTION_NORMAL;
        }

        QToolBox::tab:selected:disabled {
            background-color: COLOR_BACKGROUND_NORMAL;
            border-bottom: 2px solid COLOR_SELECTION_DARK;
        }

        QToolBox::tab:!selected {
            background-color: COLOR_BACKGROUND_NORMAL;
            border-bottom: 2px solid COLOR_BACKGROUND_NORMAL;
        }

        QToolBox::tab:!selected:disabled {
            background-color: COLOR_BACKGROUND_DARK;
        }

        QToolBox::tab:hover {
            border-color: COLOR_SELECTION_LIGHT;
            border-bottom: 2px solid COLOR_SELECTION_LIGHT;
        }

        QToolBox QScrollArea QWidget QWidget {
            padding: 0px;
            border: 0px;
            background-color: COLOR_BACKGROUND_DARK;
        }


        /* QFrame -----------------------------------------------------------------
        https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe
        https://doc.qt.io/qt-5/qframe.html#-prop
        https://doc.qt.io/qt-5/qframe.html#details
        https://stackoverflow.com/questions/14581498/qt-stylesheet-for-hline-vline-color
        --------------------------------------------------------------------------- */


        /* (dot) .QFrame  fix #141, #126, #123 */

        .QFrame {
            border-radius: SIZE_BORDER_RADIUS;
            border: 1px solid COLOR_BORDER;
            /* No frame */
        }

        .QFrame[frameShape="0"] {
            border-radius: SIZE_BORDER_RADIUS;
            border: 1px transparent COLOR_BACKGROUND_NORMAL;
            /* HLine */
        }

        .QFrame[frameShape="4"] {
            max-height: 2px;
            border: none;
            background-color: COLOR_BACKGROUND_NORMAL;
            /* HLine */
        }

        .QFrame[frameShape="5"] {
            max-width: 2px;
            border: none;
            background-color: COLOR_BACKGROUND_NORMAL;
        }


        /* QSplitter --------------------------------------------------------------
        https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsplitter
        --------------------------------------------------------------------------- */

        QSplitter {
            background-color: COLOR_BACKGROUND_NORMAL;
            spacing: 0px;
            padding: 0px;
            margin: 0px;
        }

        QSplitter::handle {
            background-color: COLOR_BACKGROUND_NORMAL;
            border: 0px solid COLOR_BACKGROUND_DARK;
            spacing: 0px;
            padding: 1px;
            margin: 0px;
        }

        QSplitter::handle:hover {
            background-color: COLOR_FOREGROUND_DARK;
        }

        QSplitter::handle:horizontal {
            width: 5px;
            image: url('./ico/rc/line_vertical.png');
        }

        QSplitter::handle:vertical {
            height: 5px;
            image: url('./ico/rc/line_horizontal.png');
        }


        /* QDateEdit, QDateTimeEdit -----------------------------------------------
        --------------------------------------------------------------------------- */

        QDateEdit,
        QDateTimeEdit {
            selection-background-color: COLOR_SELECTION_NORMAL;
            border-style: solid;
            border: 1px solid COLOR_BORDER;
            border-radius: SIZE_BORDER_RADIUS;
            /* This fixes 103, 111 */
            padding-top: 2px;
            /* This fixes 103, 111 */
            padding-bottom: 2px;
            padding-left: 4px;
            padding-right: 4px;
            min-width: 10px;
        }

        QDateEdit:on,
        QDateTimeEdit:on {
            selection-background-color: COLOR_SELECTION_NORMAL;
        }

        QDateEdit::drop-down,
        QDateTimeEdit::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 12px;
            border-left: 1px solid COLOR_BACKGROUND_NORMAL;
        }

        QDateEdit::down-arrow,
        QDateTimeEdit::down-arrow {
            image: url('./ico/rc/arrow_down_disabled.png');
            height: 8px;
            width: 8px;
        }

        QDateEdit::down-arrow:on,
        QDateTimeEdit::down-arrow:on,
        QDateEdit::down-arrow:hover,
        QDateTimeEdit::down-arrow:hover,
        QDateEdit::down-arrow:focus,
        QDateTimeEdit::down-arrow:focus {
            image: url('./ico/rc/arrow_down.png');
        }

        QDateEdit QAbstractItemView,
        QDateTimeEdit QAbstractItemView {
            background-color: COLOR_BACKGROUND_DARK;
            border-radius: SIZE_BORDER_RADIUS;
            border: 1px solid COLOR_BORDER;
            selection-background-color: COLOR_SELECTION_NORMAL;
        }


        /* QAbstractView ----------------------------------------------------------
        --------------------------------------------------------------------------- */

        QAbstractView:hover {
            border: 1px solid COLOR_SELECTION_LIGHT;
            color: COLOR_FOREGROUND_LIGHT;
        }

        QAbstractView:selected {
            background: COLOR_SELECTION_NORMAL;
            color: COLOR_BACKGROUND_NORMAL;
        }


        /* PlotWidget -------------------------------------------------------------
        --------------------------------------------------------------------------- */

        PlotWidget {
            /* Fix cut labels in plots #134 */
            padding: 0px;
        }'''
    for x in varNames.items():
        cssDefault = cssDefault.replace(x[0],x[1])
    # with open('style.css','w',encoding='utf8') as f:
    #     f.write(cssDefault)
    return cssDefault

