// Replace all instances of `StitchComponent` with your target component name.
import React from 'react';

/**
 * Props for the StitchComponent template.
 */
export interface StitchComponentProps {
  readonly children?: React.ReactNode;
  readonly className?: string;
}

/**
 * Base React component template for generated Stitch components.
 */
export const StitchComponent: React.FC<Readonly<StitchComponentProps>> = ({
  children,
  className = '',
  ...props
}) => {
  return (
    <div className={`relative ${className}`} {...props}>
      {children}
    </div>
  );
};
