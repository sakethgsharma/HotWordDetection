clc;
clear all;
close all;

no_of_filters = 23;
lowerf = 300;
upperf = 3800;
Fs = 8000;
no_of_DFT_points = 256;

mel_freq_lower = 2595*log10(1+(lowerf/700));
mel_freq_upper = 2595*log10(1+(upperf/700));

mel_spacing = (mel_freq_upper - mel_freq_lower)/(no_of_filters+1);

mel_filter_cutoffs(1) = mel_freq_lower;
for filter_no = 1:no_of_filters
    mel_filter_cutoffs(filter_no+1) = mel_freq_lower + filter_no*mel_spacing;
end
mel_filter_cutoffs(filter_no+2) = mel_freq_upper;

linear_filter_cutoffs = (10.^(mel_filter_cutoffs/2595) - 1)*700;
linear_filter_cutoffs_discrete = round(linear_filter_cutoffs*no_of_DFT_points/Fs);
%linear_filter_cutoffs_discrete(end) = linear_filter_cutoffs_discrete(end) - 1;

for i = 2:length(linear_filter_cutoffs_discrete)-1
    filter(i-1,1:no_of_DFT_points/2) = 0;
    for j = linear_filter_cutoffs_discrete(i-1):1:linear_filter_cutoffs_discrete(i+1)
        if (j == linear_filter_cutoffs_discrete(i))
            filter(i-1,j+1) = 1;
        elseif (j < linear_filter_cutoffs_discrete(i))
            filter(i-1,j+1) = (j-linear_filter_cutoffs_discrete(i-1))/(linear_filter_cutoffs_discrete(i) - linear_filter_cutoffs_discrete(i-1));
        else
            filter(i-1,j+1) = (linear_filter_cutoffs_discrete(i+1)-j)/(linear_filter_cutoffs_discrete(i+1) - linear_filter_cutoffs_discrete(i));
        end
    end
end


% plotting filter bank
cc = hsv(5);    % For color plot
for k = 1:no_of_filters
    plot(Fs/no_of_DFT_points:(1/no_of_DFT_points)*Fs:Fs/2,filter(k,:),'color',cc(mod(k,5)+1,:));
    hold on;
end
hold off;
filter = [filter zeros(no_of_filters,1)];
