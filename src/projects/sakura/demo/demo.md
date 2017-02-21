# Header level 1
## Header level 2
### Header level 3
#### Header level 4
##### Header level 5
###### Header level 6

A horizontal line:

---

Paragraphs look like this. Font size along with line height
and maximum width are optimized for reading.

*Italic*, **bold**, and `monospace`. Itemized lists
look like:

* this one
* that one
* the other one

**Here's a block quote**:

> Man surprised me most about humanity. Because he sacrifices his health in order to make money.
Then he sacrifices money to recuperate his health. And then he is so anxious about the future that he does not enjoy the present; the result being that he does not live in the present or the future; he lives as if he is never going to die, and then dies having never really lived.
> -James J Lachard

An h2 header
------------

**Some code blocks**

```
define foobar() {
    print "Welcome to flavor country!";
}
```

```python
import time
# Quick, count to ten!
for i in range(10):
    # (but not *too* quick)
    time.sleep(0.5)
    print i
```

### An h3 header ###

A nested list:

 1. First, get these ingredients:

      * carrots
      * celery
      * lentils

 2. Boil some water.

 3. Dump everything in the pot and follow
    this algorithm:

        find wooden spoon
        uncover pot
        stir
        cover pot
        balance wooden spoon precariously on pot handle
        wait 10 minutes
        goto first step (or shut off burner when done)

    Do not bump wooden spoon or it will fall.

Here's a link to [a website](http://foo.bar), to a [local
doc](local-doc.html), and to a [section heading in the current
doc](#an-h2-header). Here's a footnote [^1].

[^1]: Footnote text goes here.

Tables can look like this:

size  material      color
----  ------------  ------------
9     leather       brown
10    hemp canvas   natural
11    glass         transparent

Table: Shoes, their sizes, and what they're made of

Multi-line tables:

--------  -----------------------
keyword   text
--------  -----------------------
red       Sunsets, apples, and
          other red or reddish
          things.

green     Leaves, grass, frogs
          and other things it's
          not easy being.
--------  -----------------------

A horizontal rule follows.

***

Images are responsive by default:

![example image](sakura.png "An exemplary image")

***

# Form Elements

<form>
<fieldset id="forms__input">
<legend>Input fields</legend>
<p>
<label for="input__text">Text Input</label>
<input id="input__text" type="text" placeholder="Text Input">
</p>
<p>
<label for="input__password">Password</label>
<input id="input__password" type="password" placeholder="Type your Password">
</p>
<p>
<label for="input__webaddress">Web Address</label>
<input id="input__webaddress" type="url" placeholder="http://yoursite.com">
</p>
<p>
<label for="input__emailaddress">Email Address</label>
<input id="input__emailaddress" type="email" placeholder="name@email.com">
</p>
<p>
<label for="input__phone">Phone Number</label>
<input id="input__phone" type="tel" placeholder="(999) 999-9999">
</p>
<p>
<label for="input__search">Search</label>
<input id="input__search" type="search" placeholder="Enter Search Term">
</p>
<p>
<label for="input__text2">Number Input</label>
<input id="input__text2" type="number" placeholder="Enter a Number">
</p>
<p>
<label for="input__text3" class="error">Error</label>
<input id="input__text3" class="is-error" type="text" placeholder="Text Input">
</p>
<p>
<label for="input__text4" class="valid">Valid</label>
<input id="input__text4" class="is-valid" type="text" placeholder="Text Input">
</p>
</fieldset>
<p><a href="#top">[Top]</a></p>
<fieldset id="forms__select">
<legend>Select menus</legend>
<p>
<label for="select">Select</label>
<select id="select">
<optgroup label="Option Group">
<option>Option One</option>
<option>Option Two</option>
<option>Option Three</option>
</optgroup>
</select>
</p>
</fieldset>
<p><a href="#top">[Top]</a></p>
<fieldset id="forms__checkbox">
<legend>Checkboxes</legend>
<ul class="list list--bare">
<li><label for="checkbox1"><input id="checkbox1" name="checkbox" type="checkbox" checked="checked"> Choice A</label></li>
<li><label for="checkbox2"><input id="checkbox2" name="checkbox" type="checkbox"> Choice B</label></li>
<li><label for="checkbox3"><input id="checkbox3" name="checkbox" type="checkbox"> Choice C</label></li>
</ul>
</fieldset>
<p><a href="#top">[Top]</a></p>
<fieldset id="forms__textareas">
<legend>Textareas</legend>
<p>
<label for="textarea">Textarea</label>
<textarea id="textarea" rows="8" cols="48" placeholder="Enter your message here"></textarea>
</p>
</fieldset>
<p><a href="#top">[Top]</a></p>
<fieldset id="forms__html5">
<fieldset id="forms__action">
<legend>Action buttons</legend>
<p>
<input type="submit" value="input type=submit">
<input type="button" value="input type=button">
<input type="reset" value="input type=reset">
<input type="submit" value="input disabled" disabled>
</p>
<p>
<button type="submit">&lt;button type=submit&gt;</button>
<button type="button">&lt;button type=button&gt;</button>
<button type="reset">&lt;button type=reset&gt;</button>
<button type="button" disabled>&lt;button disabled&gt;</button>
</p>
</fieldset>
<p><a href="#top">[Top]</a></p>
</form>
