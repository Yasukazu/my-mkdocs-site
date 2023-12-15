def define_env(env):
    """
    This is the hook for the functions (new form)
    """

    @env.macro
    def with_tax_price(price, tax):
        "Calculate price with tax without trailing fractional zero"
        return ' {0:g} '.format(price * (1 + tax))
    
    @env.macro
    def lang_span(s, lang, t):
        "HTML span lang="
        return s + f"<span lang='{lang}'>{t}</span>"