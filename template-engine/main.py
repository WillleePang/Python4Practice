#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import re


class CodeBuilder(object):
    """Build source code conveniently"""

    def __init__(self, indent=0):
        self.code = []
        self.indent_level = indent

    def __str__(self):
        return "".join(str(c) for c in self.code)

    def add_line(self, line):
        """Add a line of source to the code.
        Indentation and newline will be added for you, don't provide them.
        """
        self.code.extend([" " * self.indent_level, line, "\n"])

    INDENT_STEP = 4  # PEP8 says so!

    def indent(self):
        """Increase the current indent for following lines."""
        self.indent_level += self.INDENT_STEP

    def dedent(self):
        """Decrease the current indent for following lines."""
        self.indent_level -= self.INDENT_STEP

    def add_section(self):
        """Add a section , a sub-CodeBuilder."""
        section = CodeBuilder(self.indent_level)
        self.code.append(section)
        return section

    def get_globals(self):
        """Execute the code, and return a dict of globals it defines."""
        # A check that the caller really finished all the blocks they started
        assert self.indent_level == 0
        # Get the Python source as a single string.
        python_source = str(self)
        # Execute the source, defining globals, and return them.
        global_namespace = {}
        exec (python_source, global_namespace)
        return global_namespace


class Templite(object):
    """A simple template renderer, for a nano-subset of Django syntax.
    Supported constructs are extended variable access::
        {{var.modifer.modifier|filter|filter}}
    loops::
        {% for var in list %}...{% endfor %}
    and ifs::
        {% if var %}...{% endif %}
    Comments are within curly-hash markers::
        {# This will be ignored #}
    Construct a Templite with the template text, then use `render` against a
    dictionary context to create a finished string::
        templite = Templite('''
            <h1>Hello {{name|upper}}!</h1>
            {% for topic in topics %}
                <p>You are interested in {{topic}}.</p>
            {% endif %}
            ''',
            {'upper': str.upper},
        )
        text = templite.render({
            'name': "Ned",
            'topics': ['Python', 'Geometry', 'Juggling'],
        })
    """

    def __init__(self, text, *contexts):
        """Construct a Templite with the given `text`.
        `contexts` are dictionaries of values to use for future renderins.
        These are good for filters and global values.
        """
        self.context = {}
        for context in contexts:
            context.update(context)

        self.all_vars = set()
        self.loop_vars = set()

        code = CodeBuilder()
        code.add_line("def render_function(context, do_dots):")
        code.indent()
        vars_code = code.add_section()
        code.add_line("result = []")
        code.add_line("append_result = result.append")
        code.add_line("extend_result = result.extend")
        code.add_line("to_str = str")

        buffered = []

        def flush_output():
            """Force `buffered` to the code builder."""
            if len(buffered) == 1:
                code.add_line("append_result(%s)" % buffered[0])
            elif len(buffered) > 1:
                code.add_line("extend_result([%s])" % ", ".join(buffered))
            del buffered[:]

        ops_stack = []

        tokens = re.split(r"(?s)({{.*?}}|{%.*?%}|{#.*?#})", text)

        for token in tokens:
            if token.startswith("#"):
                # Comment:ignore it and move on
                continue
            elif token.startswith('{{'):
                # An expression to evaluate
                expr = self._expr_code(token[2:-2].strip())
                buffered.append("to_str(%s)" % expr)
            elif token.startswith('{%'):
                # Action tag: split into words and parse further.
                flush_output()
                words = token[2:-2].strip().split()
                if words[0] == 'if':
                    # An if statement: evaluate the expression to determine if.
                    if len(words) != 2:
                        self._syntax_error("Don't understand if", token)
                    ops_stack.append('if')
                    code.add_line("if %s:" % self._expr_code(words[1]))
                    code.indent()
                elif words[0] == 'for':
                    # A loop :iterate over expression result.
                    if len(words) != 4 or words[2] != 'in':
                        self._syntax_error("Don't unserstand for", token)
                    ops_stack.append('for')
                    self._variable(words[1], self.loop_vars)
                    code.add_line(
                        "for c_%s in %s:" % (
                            words[1],
                            self._expr_code(words[3])
                        )
                    )


if __name__ == '__main__':
    text = "<p>Topics for {{name}}: {% for t in topics %}{#worinimei#}{{t}}, {% endfor %}</p>"
    tokens = re.split(r"(?s)({{.*?}}|{%.*?%}|{#.*?#})", text)
    for token in tokens:
        print token
