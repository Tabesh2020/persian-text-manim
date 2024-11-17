from manim import Scene, Text, UP, DOWN, Write, VGroup, FadeIn, ScaleInPlace, Rotate, PI

def create_persian_text(content, font="IRLotus", font_size=48, color="WHITE", weight=None, slant=None, **kwargs):
    # ایجاد متن با فونت فارسی و ویژگی‌های اضافی
    text = Text(content, font=font, font_size=font_size, color=color, **kwargs)
    
    # اعمال ویژگی‌های بولد و ایتالیک اگر مقداردهی شده باشند
    if weight:
        text.set_weight(weight)
    if slant:
        text.set_slant(slant)
    
    text.submobjects.reverse()  # برعکس کردن ترتیب حروف برای راست به چپ
    return text

class PersianTextScene(Scene):
    def construct(self):
        # چند خط متن فارسی با بولد و ایتالیک
        line1 = create_persian_text("اولین انیمیشن فارسی در مانیم", font="IRLotus", font_size=70, color="BLUE")
        line2 = create_persian_text("در حال ایجاد افزونه", font="IRLotus", font_size=70, color="GREEN", weight='BOLD')  # بولد
        line3 = create_persian_text("این خط ایتالیک است", font="IRLotus", font_size=70, color="RED", slant='ITALIC')  # ایتالیک

        # ترکیب خطوط
        text_group = VGroup(line1, line2, line3).arrange(DOWN).shift(UP)

        # انیمیشن‌های پیشرفته
        self.play(FadeIn(text_group))  # نمایش تدریجی متن
        self.wait(1)

        # مقیاس‌دهی به متن
        self.play(ScaleInPlace(line1, scale_factor=1.5))
        self.wait(1)

        # جابجایی متن به سمت بالا
        self.play(line1.animate.shift(UP))
        self.wait(1)

        # چرخاندن متن
        self.play(line1.animate.rotate(PI/4))  # استفاده از PI از manim
        self.wait(1)

        # نمایش متن‌های بلند
        paragraph = create_persian_text(
            "این یک متن بلند است که در چند خط قرار می‌گیرد. "
            "با استفاده از این روش می‌توانید متون طولانی را به راحتی مدیریت کنید.",
            font="IRLotus", font_size=60, color="BLACK"
        ).arrange(DOWN).shift(DOWN)
        self.play(Write(paragraph))
        self.wait(2)
