# Image_processing_project

- [Image\_processing\_project](#image_processing_project)
  - [Setup](#setup)
  - [Usage](#usage)
  - [Functionalities](#functionalities)
  - [Examples](#examples)
    - [Denoise](#denoise)
    - [Noise](#noise)

## Setup

To use this project, you first need to install the depedencies.

```
pip install -r requirements.txt
```

## Usage

To use each functionnality, simply go to the desired folder and execute the "main.py". After that, every instruction will be explained directly by the script.

Some reference images are given in the project for your testing. You can also compute the SNR ([Signal to Noise Ratio](https://en.wikipedia.org/wiki/Signal-to-noise_ratio_(imaging))) to evaluate the improvement of an image.

## Functionalities

**Denoise**
  - convolution
  - median filter

**Noise**
  - additive
  - multiplicative
  - salt and pepper
  - gaussian

**snr verification**


## Examples

### Denoise

Denoise using the median filter on an image with additive noise :
<br>
<div>
  <img src="https://github.com/Malachite01/Image_processing_project/assets/112857106/82c68b30-7fb7-4111-acd3-bcdf978ffdad" width="230">

  <figcaption>
  
  *Original SNR with noised image (Additive noise): 15.3680*
  
  </figcaption>

  <img src="https://github.com/Malachite01/Image_processing_project/assets/112857106/2c352e5c-b49e-4997-914b-79eea207acb8" width="230">

  <figcaption>
  
  *Final SNR with denoised image: 23.0485*
  
  </figcaption>
</div>

### Noise

Add noise using additive noise on an image :
<br>
<div>
  <img src="https://github.com/Malachite01/Image_processing_project/assets/112857106/d1853415-966d-4c54-bbc0-aa1779870788" width="230">

  <figcaption>
  
  *Original SNR with reference image : 16.4138*
  
  </figcaption>

  <img src="https://github.com/Malachite01/Image_processing_project/assets/112857106/316e668b-73ed-4dd4-9114-ded0ead62fee" width="230">

  <figcaption>
  
  *Final SNR with noised image (Additive noise, with a probability of 0.2): 9.7254*
  
  </figcaption>
</div>
