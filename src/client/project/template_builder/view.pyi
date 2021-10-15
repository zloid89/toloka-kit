__all__ = [
    'BaseViewV1',
    'ActionButtonViewV1',
    'AlertViewV1',
    'AudioViewV1',
    'CollapseViewV1',
    'DeviceFrameViewV1',
    'DividerViewV1',
    'GroupViewV1',
    'IframeViewV1',
    'ImageViewV1',
    'LabeledListViewV1',
    'LinkViewV1',
    'LinkGroupViewV1',
    'ListViewV1',
    'MarkdownViewV1',
    'TextViewV1',
    'VideoViewV1',
]
import toloka.client.project.template_builder.base
import toloka.util._extendable_enum
import typing


class BaseViewV1(toloka.client.project.template_builder.base.BaseComponent):
    """Elements displayed in the interface, such as text, list, audio player, or image.

    Attributes:
        label: Label above the component.
        hint: Hint text.
        validation: Validation based on condition.
    """

    def __init__(
        self,
        *,
        hint: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class BaseViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]


class ActionButtonViewV1(BaseViewV1):
    """Button that calls an action.

    When clicking the button, an action specified in the action property is called.

    Attributes:
        action: Action called when clicking the button.
        hint: Hint text.
        label: Button text.
        validation: Validation based on condition.
    """

    def __init__(
        self,
        action: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        *,
        hint: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class ActionButtonViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]
    action: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]


class AlertViewV1(BaseViewV1):
    """The component creates a color block to highlight important information.

    You can use both plain text and other visual components inside it.

    Attributes:
        content: Content of the block with important information.
        theme: Determines the block color.
        hint: Hint text.
        label: Label above the component.
        validation: Validation based on condition.
    """

    class Theme(toloka.util._extendable_enum.ExtendableStrEnum):
        """An enumeration

        Attributes:
            INFO: (default) Blue.
            SUCCESS: Green.
            WARNING: Yellow.
            DANGER: Red.
        """

        DANGER = 'danger'
        INFO = 'info'
        SUCCESS = 'success'
        WARNING = 'warning'

    def __init__(
        self,
        content: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        *,
        theme: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Theme]] = None,
        hint: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class AlertViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]
    content: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    theme: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Theme]]


class AudioViewV1(BaseViewV1):
    """The component plays audio.

    Format support depends on the user's browser, OS, and device. We recommend using MP3.

    Attributes:
        url: Audio link.
        loop: Automatically replay audio.
        hint: Hint text.
        label: Label above the component.
        validation: Validation based on condition.
    """

    def __init__(
        self,
        url: typing.Optional[typing.Any] = None,
        *,
        loop: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]] = None,
        hint: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class AudioViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]
    url: typing.Optional[typing.Any]
    loop: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]]


class CollapseViewV1(BaseViewV1):
    """Expandable block.

    Lets you add hidden content that doesn't need to be shown initially or that takes up a large space.

    The block heading is always visible.

    If you set the defaultOpened property to true, the block is expanded immediately, but it can be collapsed.

    Attributes:
        content: Content hidden in the block.
        label: Block heading.
        default_opened: If true, the block is immediately displayed in expanded form. By default, false (the block is
            collapsed).
        hint: Hint text.
        validation: Validation based on condition.
    """

    def __init__(
        self,
        content: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        *,
        label: typing.Optional[typing.Any] = None,
        default_opened: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]] = None,
        hint: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class CollapseViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]
    content: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    default_opened: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]]


class DeviceFrameViewV1(BaseViewV1):
    """Wraps the content of a component in a frame that is similar to a mobile phone.

    You can place other components inside the frame.

    Attributes:
        content: Content inside the frame.
        full_height: If true, the element takes up all the vertical free space. The element is set to a minimum height
            of 400 pixels.
        max_width: Maximum width of the element in pixels, must be greater than min_width.
        min_width: Minimum width of the element in pixels. Takes priority over max_width.
        ratio: An array of two numbers that sets the relative dimensions of the sides: width (first number) to
            height (second number). Not valid if full_height=true.
        hint: Hint text.
        label: Label above the component.
        validation: Validation based on condition.
    """

    def __init__(
        self,
        content: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        *,
        full_height: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]] = None,
        max_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]] = None,
        min_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]] = None,
        ratio: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]]] = None,
        hint: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class DeviceFrameViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]
    content: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    full_height: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]]
    max_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]
    min_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]
    ratio: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]]]


class DividerViewV1(BaseViewV1):
    """Horizontal delimiter.

    You can place extra elements in the center of the delimiter, like a popup hint and label.

    Attributes:
        hint: Hint text.
        label: A label in the center of the delimiter. Line breaks are not supported.
        validation: Validation based on condition.
    """

    def __init__(
        self,
        *,
        hint: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class DividerViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]


class GroupViewV1(BaseViewV1):
    """Groups components visually into framed blocks.

    Attributes:
        content: Content of a group block.
        hint: Explanation of the group heading. To insert a new line, use
            .
        label: Group heading.
        validation: Validation based on condition.
    """

    def __init__(
        self,
        content: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        *,
        hint: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class GroupViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]
    content: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]


class IframeViewV1(BaseViewV1):
    """Displays the web page at the URL in an iframe window.

    Attributes:
        url: URL of the web page.
        full_height: If true, the element takes up all the vertical free space. The element is set to a minimum height
            of 400 pixels.
        max_width: Maximum width of the element in pixels, must be greater than min_width.
        min_width: Minimum width of the element in pixels. Takes priority over max_width.
        ratio: An array of two numbers that sets the relative dimensions of the sides: width (first number) to
            height (second number). Not valid if full_height=true.
        hint: Hint text.
        label: Label above the component.
        validation: Validation based on condition.
    """

    def __init__(
        self,
        url: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
        *,
        full_height: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]] = None,
        max_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]] = None,
        min_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]] = None,
        ratio: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]]] = None,
        hint: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class IframeViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]
    url: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]
    full_height: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]]
    max_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]
    min_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]
    ratio: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]]]


class ImageViewV1(BaseViewV1):
    """Displays an image.

    Attributes:
        url: Image link.
        full_height: If true, the element takes up all the vertical free space. The element is set to a minimum height
            of 400 pixels.
        max_width: Maximum width of the element in pixels, must be greater than min_width.
        min_width: Minimum width of the element in pixels. Takes priority over max_width.
        no_border: Controls the display of a frame around an image. By default, true (the frame is hidden). Set false
            to display the frame.
        no_lazy_load: Disables lazy loading. If true, images start loading immediately, even if they aren't in the
            viewport. Useful for icons. By default, false (lazy loading is enabled). In this mode, images start loading
            only when they get in the user's field of view.
        popup: Specifies whether opening a full-size image with a click is allowed. By default, it is true (allowed).
        ratio: An array of two numbers that sets the relative dimensions of the sides: width (first number) to
            height (second number). Not valid if full_height=true.
        scrollable: When set to true, an image has scroll bars if it doesn't fit in the parent element.
            If false, the image fits in the parent element and, when clicked, opens in its original size in the module
            window.
            Images in SVG format with no size specified always fit in their parent elements.
        hint: Hint text.
        label: Label above the component.
        validation: Validation based on condition.
    """

    def __init__(
        self,
        url: typing.Optional[typing.Any] = None,
        *,
        full_height: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]] = None,
        max_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]] = None,
        min_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]] = None,
        no_border: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]] = None,
        no_lazy_load: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]] = None,
        popup: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]] = None,
        ratio: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]]] = None,
        rotatable: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]] = None,
        scrollable: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]] = None,
        hint: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class ImageViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]
    url: typing.Optional[typing.Any]
    full_height: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]]
    max_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]
    min_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]
    no_border: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]]
    no_lazy_load: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]]
    popup: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]]
    ratio: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]]]
    rotatable: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]]
    scrollable: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]]


class LabeledListViewV1(BaseViewV1):
    """Displaying components as a list with labels placed on the left.

    If you don't need labels, use view.list.

    Attributes:
        items: List items.
        min_width: The minimum width of list content. If the component width is less than the specified value, it
            switches to compact mode.
        hint: Hint text.
        label: Label above the component.
        validation: Validation based on condition.
    """

    class Item(toloka.client.project.template_builder.base.BaseTemplate):
        """Item.

        Attributes:
            content: List item content.
            label: A label displayed next to a list item.
            center_label: If true, a label is center-aligned relative to the content of a list item (content). Use it
                if the list consists of large items, such as images or multi-line text.
                By default, false (the label is aligned to the top of the content block).
            hint: A pop-up hint displayed next to a label.
        """

        def __init__(
            self,
            content: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
            label: typing.Optional[typing.Any] = None,
            *,
            center_label: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]] = None,
            hint: typing.Optional[typing.Any] = None
        ) -> None:
            """Method generated by attrs for class LabeledListViewV1.Item.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        content: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
        label: typing.Optional[typing.Any]
        center_label: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]]
        hint: typing.Optional[typing.Any]

    def __init__(
        self,
        items: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Item]]]] = None,
        *,
        min_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]] = None,
        hint: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class LabeledListViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]
    items: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Item]]]]
    min_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]


class LinkViewV1(BaseViewV1):
    """Universal way to add a link.

    This link changes color when clicked.

    We recommend using this component if you need to insert a link without additional formatting.

    If you want to insert a button that will open the link, use the view.action-button and action.open-link components.

    To insert a link with a search query, use helper.search-query.

    Attributes:
        url: Link URL.
        content: Link text displayed to the user.
        hint: Hint text.
        label: Label above the component.
        validation: Validation based on condition.
    """

    def __init__(
        self,
        url: typing.Optional[typing.Any] = None,
        *,
        content: typing.Optional[typing.Any] = None,
        hint: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class LinkViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]
    url: typing.Optional[typing.Any]
    content: typing.Optional[typing.Any]


class LinkGroupViewV1(BaseViewV1):
    """Puts links into groups

    The most important link in a group can be highlighted with a border: set the theme property to primary for this link.
    This only groups links, unlike GroupViewV1.

    Attributes:
        links: Array of links that make up a group.
        hint: Hint text.
        label: Label above the component.
        validation: Validation based on condition.

    Examples:
        How to add several links.

        >>> links = tb.view.LinkGroupViewV1(
        >>>     [
        >>>         tb.view.LinkGroupViewV1.Link(
        >>>             'https://any.com/useful/url/1',
        >>>             'Example1',
        >>>         ),
        >>>         tb.view.LinkGroupViewV1.Link(
        >>>             'https://any.com/useful/url/2',
        >>>             'Example2',
        >>>         ),
        >>>     ]
        >>> )
        ...
    """

    class Link(toloka.client.project.template_builder.base.BaseTemplate):
        """Link parameters

        Attributes:
            url: Link address
            content: Link text that's displayed to the user. Unviewed links are blue and underlined, and clicked links are purple.
            theme: Defines the appearance of the link. If you specify "theme": "primary", it's a button, otherwise it's a text link.
        """

        def __init__(
            self,
            url: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
            content: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
            *,
            theme: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None
        ) -> None:
            """Method generated by attrs for class LinkGroupViewV1.Link.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        url: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]
        content: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]
        theme: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]

    def __init__(
        self,
        links: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Link]]]] = None,
        *,
        hint: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class LinkGroupViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]
    links: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Link]]]]


class ListViewV1(BaseViewV1):
    """Block for displaying data in a list.

    Attributes:
        items:  Array of list items.
        direction: Determines the direction of the list.
        size: Specifies the size of the margins between elements. Acceptable values in ascending order: s, m (default
            value).
        hint: Hint text.
        label: Label above the component.
        validation: Validation based on condition.
    """

    def __init__(
        self,
        items: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[toloka.client.project.template_builder.base.BaseComponent]]] = None,
        *,
        direction: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, toloka.client.project.template_builder.base.ListDirection]] = None,
        size: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, toloka.client.project.template_builder.base.ListSize]] = None,
        hint: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class ListViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]
    items: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[toloka.client.project.template_builder.base.BaseComponent]]]
    direction: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, toloka.client.project.template_builder.base.ListDirection]]
    size: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, toloka.client.project.template_builder.base.ListSize]]


class MarkdownViewV1(BaseViewV1):
    """Block for displaying text in Markdown.

    The contents of the block are written to the content property in a single line. To insert line breaks, use \n
        Straight quotation marks (") must be escaped like this: \".

        Note that the view.markdown component is resource-intensive and might overload weak user devices.
        Do not use this component to display plain text. If you need to display text without formatting, use the view.text
        component. If you need to insert a link, use view.link, and for an image use view.image.
        Links with Markdown are appended with target="_blank" (the link opens in a new tab), as well as
        rel="noopener noreferrer"

        Attributes:
            content: Text in Markdown.

        Example:
            How to add a title and description on the task interface.

            >>> header = tb.view.MarkdownViewV1('# Some Header:
    ---
    Some detailed description')
            ...

    Attributes:
        hint: Hint text.
        label: Label above the component.
        validation: Validation based on condition.
    """

    def __init__(
        self,
        content: typing.Optional[typing.Any] = None,
        *,
        hint: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class MarkdownViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]
    content: typing.Optional[typing.Any]


class TextViewV1(BaseViewV1):
    """Block for displaying text.

    If you need formatted text, use view.markdown.

    Attributes:
        content: The text displayed in the block. To insert a new line, use 
        hint: Hint text.
        label: Label above the component.
        validation: Validation based on condition.

    Examples:
        How to show labeled field from the task inputs.

        >>> text_view = tb.view.TextViewV1(tb.data.InputData('input_field_name'), label='My label:')
        ...
    """

    def __init__(
        self,
        content: typing.Optional[typing.Any] = None,
        *,
        hint: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class TextViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]
    content: typing.Optional[typing.Any]


class VideoViewV1(BaseViewV1):
    """Player for video playback.

    The player is a rectangular block with a frame and buttons to control the video. You can set the block size using
    the ratio, fullHeight, minWidth, and maxWidth properties.

    The video resolution does not affect the size of the block — the video will fit into the block and will not be
    cropped.

    Attributes:
        url: Link to the video file.
        full_height: If true, the element takes up all the vertical free space. The element is set to a minimum height
            of 400 pixels.
        max_width: Maximum width of the element in pixels, must be greater than min_width.
        min_width: Minimum width of the element in pixels. Takes priority over max_width.
        hint: Hint text.
        label: Label above the component.
        validation: Validation based on condition.
        ratio: The aspect ratio of the video block. An array of two numbers: the first sets the width of the block and
            the second sets the height.
    """

    def __init__(
        self,
        url: typing.Optional[typing.Any] = None,
        *,
        full_height: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]] = None,
        max_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]] = None,
        min_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]] = None,
        hint: typing.Optional[typing.Any] = None,
        label: typing.Optional[typing.Any] = None,
        validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class VideoViewV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    hint: typing.Optional[typing.Any]
    label: typing.Optional[typing.Any]
    validation: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    version: typing.Optional[str]
    url: typing.Optional[typing.Any]
    full_height: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]]
    max_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]
    min_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]
