# Copyright (c) 2019 The DAML Authors. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pygments.lexer import RegexLexer
from pygments.token import *

class DAMLLexer(RegexLexer):

    name = 'DAML'
    aliases = ['daml']
    filenames = ['*.daml']

    tokens = {
        'root': [
            (r'\s', Text.Whitespace),
            (r'--.*$', Comment.Single),
            (r'\{-(.|\n)*-\}', Comment.Multiline),
            (r'#.*$', Comment.Preproc),
            (r'"[^"]*"', Literal.String),
            (r'\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d([+-][0-2]\d:[0-5]\d|Z)', Literal.Date),
            (r'[0-9]+(\.[0-9]+|c)?', Literal.Number),
            (r'\'[^\']*\'', String.Symbol),
            (r'c\'\w\'', Literal.Char),
            (r'\b(actor|agree|agreement|agrees|anytime|as|await|can|case|choose|chooses|class|submit|submitMustFail|commit|commits|nonconsuming|controller|daml|data|def|default|deriving|do|does|else|ensure|exercise|exercises|export|exported|extends|fails|fetch|hiding|if|implementing|implements|import|in|infix|infixl|infixr|instance|interface|internal|invariant|lemma|let|match|module|must|mutable|newtype|observer|of|on|private|proof|public|qualified|query|references|referencing|scenario|signatory|some|such|super|table|template|test|that|then|theorem|this|to|trait|transient|type|until|update|val|whenever|where|while)\b', Keyword),
            (r'\b(Bool|Choice|ContractId|Contract|Integer|Decimal|Party|RelTime|Scenario|Char|Text|Time|Update|Record|List|with)\b', Keyword.Type),
            (r'\\|\*|\+|\^|<>|==|/=|->|-|<|<=|>|>=|=|~>|~|&&|\|\|', Operator),
            (r'\{@|@\}|\{\||\|\}|\(|\)|\{|\}|\[|\]|\||,|;|:|::|\.\.\.', Punctuation),
            (r'\b(nil|cons|create|foldl|foldr|abort|assert|getTime|return|pass|True|False)\b', Keyword.Constant),
            (r'(\b[\w\.]+|\?\b[\w,\.]*)\b', Name),
        ]
    }



