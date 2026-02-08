Core interactive elements

Links

<a> – hyperlinks, navigation, downloads
Key attributes: href, target, rel

Buttons

<button> – primary clickable action

<input type="button">

<input type="submit">

<input type="reset">

Automation tip:
Prefer <button> → clearer semantics and easier selectors.

Input fields

<input type="text">

<input type="password">

<input type="email">

<input type="number">

<input type="search">

<input type="tel">

<input type="date">

<input type="file">

<input type="hidden"> (not visible, but impacts logic)

Selection controls

<input type="checkbox">

<input type="radio">

<select>

<option>

<optgroup>

Text areas

<textarea> – multi-line input

Form structure elements

<form> – submission boundary

<label> – improves accessibility & click targeting

<fieldset> – groups form controls

<legend> – title for a fieldset

Automation tip:
Clicking a <label> often toggles checkbox/radio reliably.

Common container elements (used heavily in modern UIs)

These don’t “do” anything by themselves but are everywhere:

<div> – generic container (very common)

<span> – inline container

<section>

<article>

<header>

<footer>

<nav>

<main>

Modern frameworks often attach click handlers to <div> or <span>.

Tables & data display

<table>

<thead>

<tbody>

<tr>

<th>

<td>

Used a lot in enterprise apps and reports.

Media elements

<img>

<video>

<audio>

<source>

Automation tip:
Images are often clickable even without <a>.

Lists

<ul> – unordered list

<ol> – ordered list

<li> – list item

Menus and dropdowns are often built using lists.

Special elements to watch for
Iframes

<iframe> – embedded document
Automation requires context switching.

SVG elements

<svg>, <path>, <circle>, etc.
Common in icons, charts, custom buttons.

Custom / framework components

<custom-element>

<mat-button>

<ion-item>

<app-root>

These are Web Components or framework abstractions — selectors usually rely on attributes, roles, or nested elements.

Attributes you MUST know for automation

Regardless of tag:

id

name

class

data-* (best for automation)

role

aria-*

type

value

disabled

readonly

placeholder

What actually matters most in automation

Behavior, not tag name

Stable attributes (id, data-testid)

Visibility & state

DOM hierarchy

Events attached via JS

If you want, next we can: