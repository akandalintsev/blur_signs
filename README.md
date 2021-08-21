* Исправить в : `/moviepy/video/fx/headblur.py:38`
```
        im = gf(t)
        im = copy(im)
```

* Ручная отметка траектории блюра: `record.py`
* Размытие по созданной траектории: `edit_video.py`