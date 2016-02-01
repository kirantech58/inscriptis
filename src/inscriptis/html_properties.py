#!/usr/bin/env python3
# encoding: utf-8

class Display(object):
    inline = 1
    block = 2
    none = 3

class WhiteSpace(object):
    normal = 1 # sequences of whitespace will collapse into a single one
    pre = 3    # sequences of whitespace will be preserved

class Line(object):
    '''
    Object used to represent a line
    '''
    __slots__ = ('margin_before', 'margin_after', 'prefix', 'suffix',
                 'content', 'list_bullet', 'padding')

    def __init__(self):
        self.margin_before = 0
        self.margin_after = 0
        self.prefix = ""
        self.suffix = ""
        self.content = ""
        self.list_bullet = ""
        self.padding = 0

    def extract_pre_text(self):
        pass

    def __str__(self):
        # print(">>" + self.content + "<< before: " + str(self.margin_before) + ", after: " + str(self.margin_after) + ", padding: ", self.padding, ", list: ", self.list_bullet)
        return ''.join(('\n' * self.margin_before,
                        ' ' * (self.padding - len(self.list_bullet)),
                        self.list_bullet,
                        self.prefix,
                        ' '.join(self.content.split()),
                        self.suffix,
                        '\n' * self.margin_after))

class Table(object):
    ''' A HTML table. '''

    __slot__ = ('rows', )

    def __init__(self):
        self.rows = []

    def add_row(self):
        self.rows.append(Row())

    def add_column(self):
        if not self.rows:
            self.add_row()
        self.rows[-1].columns.append(Line)

    def add_text(self, text):
        ''' adds text to the current column '''
        self.rows[-1].columns[-1].content += text

    def __str__(self):
        '''
            ::returns:
            a rendered string representation of the given table
        '''
        return '\n'.join((str(row) for row in self.rows))

class Row(object):
    ''' A single row within a table '''
    __slot__ = ('columns', )

    def __init__(self):
        self.columns = []

    def __str__(self):
        '''
            ::returns:
            a rendered string representation of the given row
        '''
        return '\t'.join(self.columns)

