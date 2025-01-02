BASE-CSS
:root {
    --white-color: #fff;
    --black-color: #000;
    --text-color: #333;
    --primary-color: #6d2bc4c5;
    --border-color: #dbdbdb;
    --star-gold-color: #fadc31;
    --header-height: 140px;
    --navbar-height: 34px;
    --header-with-search-height: calc(var(var(--header-height) - var(--navbar-height)));
}

* {
    /* inherit: kế thừa */
    box-sizing: inherit;
    margin: 0;
}

html {
    font-size: 62.5%;
    line-height: 1.6rem;
    font-family:"Roboto", sans-serif;
    box-sizing: border-box;
}
/* Responsive */
.grid {
    /*với màn hình có kích thước nhỏ hơn 1200  thì cái max-width */
    /* giảm kích thước grid bằng kích thước của màn hình nhỏ hơn 1200  */
    width: 1200px;
    max-width: 100%;
    margin: 0 auto;
}

.grid__full-width {
    width: 100%;
}

.grid__row {
    display: flex;
    flex-wrap: wrap;
    margin-left: -5px;
    margin-right: -5px;
}

/* Test */
.grid__column-2 {
    padding-left: 5px;
    padding-right: 5px;
    width: 16.6667%;
}

.grid__column-2-4{
    padding-left: 5px;
    padding-right: 5px;
    width: 20%;
}

.grid__column-10 {
    padding-left: 5px;
    padding-right: 5px;
    width: 83.3334%;
}

/* Animation */
@keyframes fadeIn {
    from {
        opacity: 0; 
    }
    to {
        opacity: 1;
    }
}

@keyframes growth {
    from {
        transform: scale(var(--growth-from));
    }
    to {
        transform: scale(var(--growth-to));
    }
}
/* google */
.fa-google {
    background: conic-gradient(from -45deg, #ea4335 110deg, #4285f4 90deg 180deg, #34a853 180deg 270deg, #fbbc05 270deg) 73% 55%/150% 150% no-repeat;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    -webkit-text-fill-color: transparent;
  }
  
  
/* button style */

.btn {
    min-width: 124px;
    height: 34px;
    text-decoration: none;
    border: none;
    border-radius: 2px;
    font-size: 1.4rem;
    padding: 0 12px;
    cursor: pointer;
    color: var(--text-color);   
    outline: none;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    line-height: 1.6rem;
}

.btn.btn--normal:hover {
    background-color: rgba(0, 0, 0, 0.05);
}

.btn.btn--primary {
    background-color: var(--primary-color);
    color: var(--white-color);
}

.btn.btn--disabled {
    cursor: default;
    background-color: #999;
    color: #949494;
}

.btn.btn--size-s {
    height: 32px;
    font-size: 12px;
    padding: 0 8px;
}

/* Modal css */
.modal {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    display: flex;
    height: auto;
    animation: fadeIn linear 0.1s;  
    /* display: none; */
}

.modal__overlay {
    position: absolute;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.4);
}

.modal__body {
    --growth-from: 0.7;
    --growth-to : 1;
    margin: auto;
    position: relative;
    z-index: 1;
    animation: growth linear 0.1s;
}

/* Selection */
.select-input {
    position: relative;
    height: 34px;
    min-width: 200px;
    padding: 0 12px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-radius: 2px;
    background-color: var(--white-color);
    z-index: 1;
}

.select-input:hover .select-input__list {
    display: block;
}

.select-input__label {
    font-size: 1.4rem;
}

.select-input__icon {
    color: rgb(131, 131, 131);
    font-size: 1.4rem;
    position: relative;
    top: 1px;
}

.select-input__list {
    position: absolute;
    left: 0;
    right: 0;
    top: 36px;
    border-radius: 2px;
    background-color: var(--white-color);
    padding: 10px 16px;
    list-style: none;
    display: none;
}

.select-input__link {
    display: block;
    font-size: 1.4rem;
    padding: 8px 0;
    text-decoration: none;
    color: var(--text-color);
    transition: background-color 0.3s ease;
}

.select-input__link:hover {
    color: var(--primary-color);
}

