<div class="tl-unit-content ">
		<center><div class="readability"><h1 id="assignment-superpy">Assignment: SuperPy</h1>
<div class="wincpy">
<p><code class="interpreted-text" role="command">wincpy start a2bc36ea784242e4989deb157d527ba0</code></p>
</div>
<div class="prerequisites">
<p>You need to master the following to complete this assignment:</p>
<ul>
<li>Independently designing logic flow based on a description of what the program should do;</li>
<li>Using and debugging Python classes;</li>
<li>Writing, running and interpreting tests in Pytest.</li>
</ul>
</div>
<p>This is your biggest Python assignment so far, so get comfortable! It is supposed to take you a couple days to complete. You are going to build a <code class="interpreted-text" role="term">command-line tool</code> that a supermarket will use to keep track of their inventory.</p>
<p>There are three important modules from the standard library you must use for this:</p>
<ol type="1">
<li>
<p><a href="https://docs.python.org/3/library/csv.html">csv -- CSV File Reading and Writing</a></p>
<p>CSV stands for 'comma separated values'. It's the most common import and export format for spreadsheets and databases, used by -- or at least compatible with -- every software
package you can think of in that space. It is a great skill to be able to read, manipulate and write these files.</p>
</li>
<li>
<p><a href="https://docs.python.org/3/library/argparse.html">argparse -- Parser for command-line options, arguments and subcommands</a></p>
<p>Command-line tools are tools you've probably used a lot already. Examples that may be familiar to you are <code>ls</code> to show the contents of a directory and
<code>cd</code> to change the working directory. Another common tool is <code>echo</code> to parse and output some input you give it (try <code>echo "hello world"</code>).</p>
<p>There are three command-line fundamentals you should search the web for before you dive into the exercise:</p>
<ul>
<li><code class="interpreted-text" role="term">stdin</code></li>
<li><code class="interpreted-text" role="term">stdout</code></li>
<li><code class="interpreted-text" role="term">command-line arguments</code></li>
</ul>
<p>The argparse module helps you to write your own command-line tool. Now that you know about command-line arguments, you should be able to see why it's named
<em>argparse</em>.</p>
</li>
<li>
<p><a href="https://docs.python.org/3/library/datetime.html">datetime -- Basic date and time types</a></p>
<p>Dates are notoriously hard to work with in software. The list of things to consider includes timezones, daylight saving time, leap years and of course countless different
notation styles. We will standardize on a single source of truth: the <code>date</code> object, and use a string representation following the format: <code>'%Y-%m-%d'</code>. Read
the linked documentation to learn how to use these two facts!</p>
</li>
</ol>
<h2 id="superpy">SuperPy</h2>
<p>A large supermarket chain has asked you to write a command-line tool that is able to keep track of their inventory: they want to call it <strong>SuperPy</strong>. The core
functionality is about keeping track and producing reports on various kinds of data:</p>
<ul>
<li>Which products the supermarket offers;</li>
<li>How many of each type of product the supermarket holds currently;</li>
<li>How much each product was bought for, and what its expiry date is;</li>
<li>How much each product was sold for <strong>or</strong> if it expired, the fact that it did;</li>
</ul>
<p>All data must be saved in CSV files. Feel free to come up with your own file structure, but here's an example structure to get started with if you want:</p>
<table>
<thead>
<tr class="header">
<th>Filename</th>
<th>Columns</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>bought.csv</code></td>
<td><code>id,product_name,buy_date,buy_price,expiration_date</code></td>
</tr>
<tr class="even">
<td><code>sold.csv</code></td>
<td><code>id,bought_id,sell_date,sell_price</code></td>
</tr>
</tbody>
</table>
<div class="note">
<div class="title">
<p>Note</p>
</div>
<p>In this example structure, the <code>id</code> column is an integer that is incremented for each line. This allows for some clever matching of items between different tables.
You will later see this pattern a lot in databases, where it is particularly powerful.</p>
</div>
<p>Your program should have an internal conception of what day it is -- perhaps saved to a simple text file -- that we can advance time by two days by using a command like:</p>
<p><code class="interpreted-text" role="command">$ python super.py --advance-time 2</code></p>
<p>Interaction with your program must go through the command-line. Here's an example of what a sequence of interactions could look like:</p>
<pre class=""><code>$ python super.py buy --product-name orange --price 0.8 --expiration-date 2020-01-01
OK

$ python super.py report inventory --now
+--------------+-------+-----------+-----------------+
| Product Name | Count | Buy Price | Expiration Date |
+==============+=======+===========+=================+
| Orange       | 1     | 0.8       | 2020-01-01      |
+--------------+-------+-----------+-----------------+

$ python super.py --advance-time 2
OK

$ python super.py report inventory --yesterday
+--------------+-------+-----------+-----------------+
| Product Name | Count | Buy Price | Expiration Date |
+==============+=======+===========+=================+
| Orange       | 1     | 0.8       | 2020-01-01      |
+--------------+-------+-----------+-----------------+

$ python super.py sell --product-name orange --price 2
OK

$ python super.py report inventory --now
+--------------+-------+-----------+-----------------+
| Product Name | Count | Buy Price | Expiration Date |
+==============+=======+===========+=================+


$ python super.py report revenue --yesterday
Yesterday's revenue: 0

$ python super.py report revenue --today
Today's revenue so far: 2

$ python super.py report revenue --date 2019-12
Revenue from December 2019: 0

$ python super.py report profit --today
1.2

$ python super.py sell --product-name orange --price 2
ERROR: Product not in stock.</code></pre>
<h2 id="requirements">Requirements</h2>
<h3 id="code">Code</h3>
<p>Be creative with your implementation! We intentionally keep the specification open to encourage you to be creative with this project. However, to obtain a passing grade, you
will at least need to satisfy the following requirements:</p>
<ul>
<li>Well-structured and documented code, including:
<ul>
<li>Clear and effective variable and function names;</li>
<li>Use of comments where the code does not speak for itself;</li>
<li>Clear and effective separation of code into separate functions and possibly files.</li>
</ul>
</li>
<li>Use of modules to the extent that it shows you were able to independently read and understand the documentation, and apply the techniques within:
<ul>
<li><strong>csv</strong></li>
<li><strong>argparse</strong></li>
<li>
<dl>
<dt><strong>datetime</strong>, including in particular the <code>date</code> object, <code>strftime</code></dt>
<dd>
<p>and <code>strptime</code> functions and datetime arithmetic using <code>timedelta</code>.</p>
</dd>
</dl>
</li>
</ul>
</li>
<li>Use of external text files (CSV) to read and write data.</li>
<li>A well-structured and user friendly command-line interface with clear descriptions of each argument in the <code>--help</code> section.</li>
<li>A text file containing a usage guide aimed with peers as the target audience. The usage guide should include plenty of examples.</li>
<li>The application must support:
<ul>
<li>Setting and advancing the date that the application perceives as 'today';</li>
<li>Recording the buying and selling of products on certain dates;</li>
<li>Reporting revenue and profit over specified time periods;</li>
<li>Exporting selections of data to CSV files;</li>
<li>Two other additional non-trivial features of your choice, for example:
<ul>
<li>The use of an external module <a href="https://github.com/willmcgugan/rich">Rich</a> to improve the application.</li>
<li>The ability to import/export reports from/to formats other than CSV (in addition to CSV)</li>
<li>The ability to visualize some statistics using <a href="https://matplotlib.org/">Matplotlib</a></li>
<li>Another feature that you thought of.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="report">Report</h3>
<p>Please include a short, 300-word report that highlights three technical elements of your implementation that you find notable, explain what problem they solve and why you chose
to implement it in this way. Include this in your repository as a <code class="interpreted-text" role="file">report.md</code> file.</p>
<ul>
<li>You may use Markdown for your report, but it is not required.</li>
<li>To assist your explanation you may use code snippets.</li>
</ul></div></center>			</div>
