/*********************************************************************
 * @file   InspectLabelPol.h
 * @brief  ��ǩ��PolMark��λ����㷨
 * 
 * @author 
 * @date   2024.7
 *********************************************************************/
#pragma once
#include<opencv2\opencv.hpp>
#include "Define.h"

/**
 * PolMark����.
 */
enum PolMarkType
{
	E_POL_NUM = 0,	// polmark ����
	E_POL_SIGN      // polmark ����
};

/**
 * PolMarkģ��ƥ����.
 */
struct stPolMatchInfo
{
	double score = 0;
	std::string name;
	cv::Point loc;
	cv::Mat templateImg;
};


class InspectLabelPol
{
public:
	InspectLabelPol();
	~InspectLabelPol();

	/**
	 * ��λ��ǩ��PolMark.
	 * 
	 * @param src ����ͼ��(��ת����
	 * @param params ��������ṹ�壬������λ������polmarkģ��
	 * @param labelMarkInfo ��������������ǩ��PolMark��Ϣ
	 * @return �ɹ�����0�����򷵻�-1
	 */
	long DoFindLabelMark(cv::Mat src, STRU_LabelMarkParams& params, STRU_LabelMarkInfo& labelMarkInfo);

	/**
	 * ����ǩ��PolMark����.
	 * 
	 * @param image ����ͼ��(��ת����
	 * @param params ��������ṹ�壬������λ������polmarkģ��
	 * @param labelMarkInfo ͨ��DoFindLabelMark�õ��ı�ǩ��Polmark��Ϣ
	 * @return �ɹ�����0�����򷵻ش�����
	 */
	long DoFillLabelMark(cv::Mat& image, STRU_LabelMarkParams& params, const STRU_LabelMarkInfo& labelMarkInfo);

private:
	long PolMarkRec(const cv::Mat& srcImg, std::map<std::string, cv::Mat>& templates, stPolMatchInfo& polMatchInfo, PolMarkType polType);
	long DoFillLabel(cv::Mat& dstImg, const STRU_LabelMarkInfo& labelMarkInfo);
	long DoFillPolArea(cv::Mat& dstImg, STRU_LabelMarkParams& params, const STRU_LabelMarkInfo& labelMarkInfo, PolMarkType polType);

	std::vector<cv::Rect> GetPolRefRect(cv::Mat dstImg, cv::Rect& maskRect, const STRU_LabelMarkInfo& labelMarkInfo, PolMarkType polType);
	long PartialFill(cv::Mat& dstImg, cv::Rect& maskRect, std::vector<cv::Rect>& refRect);
	cv::Mat CalcProjection(const cv::Mat& srcImg, int mode);
	std::vector<int> CalcLighterPos(const cv::Mat projImg, int mode);
	double CalcMeanGrayX(const cv::Mat& src, const std::vector<int>& pos, int count, int posY);
	double CalcMeanGrayY(const cv::Mat& src, const std::vector<int>& pos, int count, int posX);
};

